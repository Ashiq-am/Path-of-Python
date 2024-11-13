class Node:
	def __init__(self):
		self.dec = False # Indicates if the subarray is decreasing
		self.inc = False # Indicates if the subarray is increasing
		self.lm = -1	 # The leftmost element of the subarray
		self.rm = -1	 # The rightmost element of the subarray


class Solution:
	def __init__(self):
		self.seg = [] # The segment tree

	# Function to merge two nodes in the segment tree
	def merge(self, n1, n2):
		# If either of the nodes represents an empty
		# subarray, return the other node
		if n1.lm == -1 or n2.lm == -1:
			return n2 if n1.lm == -1 else n1

		# Merge information from two nodes to update the
		# parent node
		ans = Node()
		ans.lm = n1.lm
		ans.rm = n2.rm
		if n1.inc and n2.inc and n1.rm <= n2.lm:
			ans.inc = True
		if n1.dec and n2.dec and n1.rm >= n2.lm:
			ans.dec = True
		return ans

	# Function to update the segment tree
	def update(self, idx, l, r, id, val):
		# If the leaf node is reached, update it with the
		# new value
		if l == r:
			self.seg[idx] = Node()
			self.seg[idx].dec = True
			self.seg[idx].inc = True
			self.seg[idx].lm = val
			self.seg[idx].rm = val
			return

		# Otherwise, recursively update the appropriate
		# child node
		mid = (l + r) // 2
		if id <= mid:
			self.update(2 * idx + 1, l, mid, id, val)
		else:
			self.update(2 * idx + 2, mid + 1, r, id, val)

		# After updating the child nodes, merge their
		# information to update the current node
		self.seg[idx] = self.merge(self.seg[2 * idx + 1], self.seg[2 * idx + 2])

	# Function to perform a query on the segment tree
	def query(self, idx, l, r, ql, qr):
		# If the current segment is completely outside the
		# query range, return an empty node
		if ql > r or qr < l:
			return Node()

		# If the current segment is completely inside the
		# query range, return the node representing it
		if ql <= l and qr >= r:
			return self.seg[idx]

		# Otherwise, recursively query the child nodes and
		# merge their information
		mid = (l + r) // 2
		lq = self.query(2 * idx + 1, l, mid, ql, qr)
		rq = self.query(2 * idx + 2, mid + 1, r, ql, qr)
		return self.merge(lq, rq)

	# Function to solve the queries
	def solveQueries(self, nums, queries):
		ans = []
		n = len(nums)
		self.seg = [Node()] * (4 * n + 1) # Resize the segment tree to accommodate the given array

		# Initializing the segment tree with the initial
		# array
		for i in range(n):
			self.update(0, 0, n - 1, i, nums[i])

		# Processing each query
		for it in queries:
			q, a, b = it
			a -= 1
			b -= 1
			if q == 1:
				# Update query: Increment the value at
				# index 'a' by 'b'
				self.update(0, 0, n - 1, a, b + 1)
			else:
				# Subarray query: Check properties of the
				# subarray from index 'a' to 'b'
				res = self.query(0, 0, n - 1, a, b)
				if res.inc == res.dec:
					ans.append(-1) # Both increasing and decreasing
				elif res.dec:
					ans.append(1) # Only decreasing
				else:
					ans.append(0) # Only increasing
		return ans


solution = Solution()
nums = [1, 5, 7, 4, 3, 5, 9]
queries = [[2, 1, 3], [1, 7, 4], [2, 6, 7]]
result = solution.solveQueries(nums, queries)

print("Result:", " ".join(map(str, result)))
