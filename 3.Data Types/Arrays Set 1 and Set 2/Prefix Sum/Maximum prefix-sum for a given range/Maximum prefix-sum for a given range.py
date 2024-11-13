# Python3 program to find
# maximum prefix sum

# struct two store two values in one node

# function to build the segment tree
def build(a, index, beg, end):
	global tree

	if (beg == end):

		# If there is one element in array,
		# store it in current node of
		# segment tree
		tree[index][0] = a[beg]
		tree[index][1] = a[beg]
	else:
		mid = (beg + end) // 2

		# If there are more than one elements,
		# then recur for left and right subtrees
		build(a, 2 * index + 1, beg, mid)
		build(a, 2 * index + 2, mid + 1, end)

		# adds the sum and stores in the index
		# position of segment tree
		tree[index][0] = tree[2 * index + 1][0] + tree[2 * index + 2][0]

		# stores the max of prefix-sum either
		# from right or from left.
		tree[index][1] = max(tree[2 * index + 1][1],tree[2 * index + 1][0] + tree[2 * index + 2][1])

# function to do the range query in the segment
# tree for the maximum prefix sum
def query(index, beg, end, l, r):
	global tree
	result = [-1, -1]
	# result[0] = result[1] = -1

	# If segment of this node is outside the given
	# range, then return the minimum value.
	if (beg > r or end < l):
		return result

	# If segment of this node is a part of given
	# range, then return the node of the segment
	if (beg >= l and end <= r):
		return tree[index]

	mid = (beg + end) // 2

	# if left segment of this node falls out of
	# range, then recur in the right side of
	# the tree
	if (l > mid):
		return query(2 * index + 2, mid + 1, end, l, r)

	# if right segment of this node falls out of
	# range, then recur in the left side of
	# the tree
	if (r <= mid):
		return query(2 * index + 1, beg, mid, l, r)

	# If a part of this segment overlaps with
	# the given range
	left = query(2 * index + 1, beg, mid, l, r)
	right = query(2 * index + 2, mid + 1, end, l, r)

	# adds the sum of the left and right
	# segment
	result[0] = left[0] + right[0]

	# stores the max of prefix-sum
	result[1] = max(left[1], left[0] + right[1])

	# returns the value
	return result


# driver program to test the program
if __name__ == '__main__':

	a = [-2, -3, 4, -1, -2, 1, 5, -3 ]

	tree = [[0,0] for i in range(4 * 10000)]

	# calculates the length of array
	n = len(a)

	# calls the build function to build
	# the segment tree
	build(a, 0, 0, n - 1)

	# find the max prefix-sum between
	# 3rd and 5th index of array
	print(query(0, 0, n - 1, 3, 5)[1])

	# find the max prefix-sum between
	# 0th and 7th index of array
	print(query(0, 0, n - 1, 1, 7)[1])

	# This code is contributed by mohit kumar 29.
