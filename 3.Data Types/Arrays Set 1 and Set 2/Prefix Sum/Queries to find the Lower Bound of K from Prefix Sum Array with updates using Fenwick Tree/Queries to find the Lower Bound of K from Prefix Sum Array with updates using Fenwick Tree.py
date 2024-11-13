# Python3 program to implement
# the above appraoch

# Function to calculate and return
# the sum of arr[0..index]
def getSum(BITree, index):

	ans = 0
	index += 1

	# Traverse ancestors
	# of BITree[index]
	while (index > 0):

		# Update the sum of current
		# element of BIT to ans
		ans += BITree[index]

		# Update index to that
		# of the parent node in
		# getSum() view by
		# subtracting LSB(Least
		# Significant Bit)
		index -= index & (-index)

	return ans

# Function to update the
# Binary Index Tree by
# replacing all ancestores
# of index by their respective
# sum with val
def updateBIT(BITree, n,
			index, val):

	index = index + 1

	# Traverse all ancestors
	# and sum with 'val'.
	while (index <= n):

		# Add 'val' to current
		# node of BIT
		BITree[index] += val

		# Update index to that
		# of the parent node in
		# updateBit() view by
		# adding LSB(Least
		# Significant Bit)
		index += index & (-index)

# Function to construct the Binary
# Indexed Tree for the given array
def constructBITree(arr, n):

	# Initialize the
	# Binary Indexed Tree
	BITree = [0] * (n + 1)

	for i in range(n + 1):
		BITree[i] = 0

	# Store the actual values in
	# BITree[] using update()
	for i in range(n):
		updateBIT(BITree, n, i, arr[i])

	return BITree

# Function to obtian and return
# the index of lower_bound of k
def getLowerBound(BITree, arr,
				n, k):

	lb = -1
	l = 0
	r = n - 1

	while (l <= r):
		mid = l + (r - l) // 2
		if (getSum(BITree,
				mid) >= k):
			r = mid - 1
			lb = mid
		else:
			l = mid + 1

	return lb

def performQueries(A, n, q):

	# Store the Binary Indexed Tree
	BITree = constructBITree(A, n)

	# Solve each query in Q
	for i in range(len(q)):
		id = q[i][0]

		if (id == 1):
			idx = q[i][1]
			val = q[i][2]
			A[idx] += val

			# Update the values of all
			# ancestors of idx
			updateBIT(BITree, n,
					idx, val)
		else:

			k = q[i][1]
			lb = getLowerBound(BITree,
							A, n, k)
			print(lb)

# Driver Code
if __name__ == "__main__":

	A = [1, 2, 3, 5, 8]
	n = len(A)
	q = [[1, 0, 2],
		[2, 5, 0],
		[1, 3, 5]]
	performQueries(A, n, q)
