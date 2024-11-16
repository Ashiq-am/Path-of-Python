class SegmentTree:
	@staticmethod
	def build(a, b, v, tl, tr):
		"""
		Function to build the segment tree recursively.

		Parameters:
			a (list): The original array.
			b (list): The segment tree array.
			v (int): Current node in the segment tree.
			tl (int): Left index of the current segment.
			tr (int): Right index of the current segment.
		"""
		# If the range has only one element, assign the value to the corresponding position in b and return
		if tl == tr:
			b[v] = a[tl]
			return

		# Calculate the middle index of the range
		tm = (tl + tr) // 2

		# Recursively build left and right subtrees
		SegmentTree.build(a, b, v * 2, tl, tm)
		SegmentTree.build(a, b, v * 2 + 1, tm + 1, tr)

		# Set the value of the current node 'v' in b to 0 (You may need to adjust this assignment based on your use case)
		b[v] = 0

	@staticmethod
	def main():
		a = [3, 5, 1, 7, 2]
		b = [0] * (4 * len(a)) # 'b' is initialized with zeros

		# Build the segment tree
		SegmentTree.build(a, b, 1, 0, len(a) - 1)

		# The resulting 'b' array will contain the segment tree structure based on array 'a'
		for value in b:
			print(value)


# Call the main method
SegmentTree.main()
