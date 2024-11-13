# Python3 program to find triplets
# a[i]>a[j]>a[k] and i<j<k
from bisect import bisect_left as lower_bound

# Updates a node in Binary Index Tree (BIT)
# at given index(i) in BIT. The given value
# 'val' is added to BITree[i] and
# all of its ancestors in tree.
def update(BIT, n, i, val):
	while i <= n:
		BIT[i] += val

		i += (i & -i)

# Returns sum of arr[0..i]. This function
# assumes that the array is preprocessed
# and partial sums of array elements are
# stored in BIT[].
def query(BIT, i):
	summ = 0
	while i > 0:
		summ += BIT[i]

		i -= (i & -i)

	return summ

# Converts an array to an array with values
# from 1 to n and relative order of smaller
# and greater elements remains same. For example,
# {7, -90, 100, 1} is converted to {3, 1, 4 ,2 }
def convert(arr, n):
	temp = [0] * n
	for i in range(n):
		temp[i] = arr[i]

	temp.sort()

	for i in range(n):
		arr[i] = lower_bound(temp, arr[i]) + 1

# Function to find triplets
def getCount(arr, n):

	# Decomposition
	convert(arr, n)

	BIT = [0] * (n + 1)
	smaller_right = [0] * (n + 1)
	greater_left = [0] * (n + 1)

	# Find all right side smaller elements
	for i in range(n - 1, -1, -1):
		smaller_right[i] = query(BIT, arr[i] - 1)
		update(BIT, n, arr[i], 1)

	for i in range(n + 1):
		BIT[i] = 0

	# Find all left side greater elements
	for i in range(n):
		greater_left[i] = i - query(BIT, arr[i])
		update(BIT, n, arr[i], 1)

	# Find the required answer
	ans = 0
	for i in range(n):
		ans += greater_left[i] * smaller_right[i]

	# Return the required answer
	return ans

# Driver Code
if __name__ == "__main__":
	arr = [7, 3, 4, 3, 3, 1]
	n = len(arr)

	print(getCount(arr, n))

# This code is contributed by
# sanjeev2552
