# Python3 program for the above approach

# Function to find the maximum and
# minimum array elements up to the i-th index
def prefixArr(arr, prefix, N):

	# Traverse the array
	for i in range(N):
		if (i == 0):
			prefix[i][0] = arr[i]
			prefix[i][1] = arr[i]

		else:

			# Compare current value with maximum
			# and minimum values up to previous index
			prefix[i][0] = max(prefix[i - 1][0], arr[i])
			prefix[i][1] = min(prefix[i - 1][1], arr[i])
	return prefix


# Function to find the maximum and
# minimum array elements from i-th index
def suffixArr(arr, suffix, N):

	# Traverse the array in reverse
	for i in range(N - 1, -1, -1):

		if (i == N - 1):
			suffix[i][0] = arr[i]
			suffix[i][1] = arr[i]

		else:

			# Compare current value with maximum
			# and minimum values in the next index
			suffix[i][0] = max(suffix[i + 1][0], arr[i])
			suffix[i][1] = min(suffix[i + 1][1], arr[i])
	return suffix

# Function to find the maximum and
# minimum array elements for each query
def maxAndmin(prefix, suffix, N, L, R):
	maximum, minimum = 0, 0

	# If no index remains after
	# excluding the elements
	# in a given range
	if (L == 0 and R == N - 1):
		print("No maximum and minimum value")
		return

	# Find maximum and minimum from
	# from the range [R + 1, N - 1]
	elif (L == 0):
		maximum = suffix[R + 1][0]
		minimum = suffix[R + 1][1]

	# Find maximum and minimum from
	# from the range [0, N - 1]
	elif (R == N - 1):
		maximum = prefix[L - 1][0]
		minimum = prefix[R - 1][1]

	# Find maximum and minimum values from the
	# ranges [0, L - 1] and [R + 1, N - 1]
	else:
		maximum = max(prefix[L - 1][0], suffix[R + 1][0])
		minimum = min(prefix[L - 1][1], suffix[R + 1][1])

	# Print maximum and minimum value
	print(maximum, minimum)

# Function to perform queries to find the
# minimum and maximum array elements excluding
# elements from a given range
def MinMaxQueries(a, queries):

	# Size of the array
	N = len(arr)

	# Size of query array
	q = len(queries)

	# prefix[i][0]: Stores the maximum
	# prefix[i][1]: Stores the minimum value
	prefix = [ [ 0 for i in range(2)] for i in range(N)]

	# suffix[i][0]: Stores the maximum
	# suffix[i][1]: Stores the minimum value
	suffix = [ [ 0 for i in range(2)] for i in range(N)]

	# Function calls to store
	# maximum and minimum values
	# for respective ranges
	prefix = prefixArr(arr, prefix, N)
	suffix = suffixArr(arr, suffix, N)

	for i in range(q):
		L = queries[i][0]
		R = queries[i][1]

		maxAndmin(prefix, suffix, N, L, R)

# Driver Code
if __name__ == '__main__':

	# Given array
	arr = [ 2, 3, 1, 8, 3, 5, 7, 4 ]
	queries = [ [ 4, 6 ], [ 0, 4 ], [ 3, 7 ], [ 2, 5 ] ]
	MinMaxQueries(arr, queries)

	# This code is contributed by mohit kumar 29.
