# Python3 implementation of above approach

def sumArray(arr, n):

	# Allocate memory for temporary arrays
	# leftSum[], rightSum[] and Sum[]
	leftSum = [0 for i in range(n)]
	rightSum = [0 for i in range(n)]
	Sum = [0 for i in range(n)]
	i, j = 0, 0

	# Left most element of left
	# array is always 0
	leftSum[0] = 0

	# Rightmost most element of right
	# array is always 0
	rightSum[n - 1] = 0

	# Construct the left array
	for i in range(1, n):
		leftSum[i] = arr[i - 1] + leftSum[i - 1]

	# Construct the right array
	for j in range(n - 2, -1, -1):
		rightSum[j] = arr[j + 1] + rightSum[j + 1]

	# Construct the sum array using
	# left[] and right[]
	for i in range(0, n):
		Sum[i] = leftSum[i] + rightSum[i]

	# print the constructed prod array
	for i in range(n):
		print(Sum[i], end = " ")


# Driver Code
arr = [3, 6, 4, 8, 9]
n = len(arr)
sumArray(arr, n)

# This code is contributed by
# mohit kumar 29
