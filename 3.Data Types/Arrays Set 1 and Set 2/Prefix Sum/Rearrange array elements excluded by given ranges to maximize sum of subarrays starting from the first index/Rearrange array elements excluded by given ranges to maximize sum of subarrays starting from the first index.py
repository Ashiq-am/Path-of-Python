# Python3 program for the
# above approach

# Function that finds the
# maximum sum all subarrays
# from the starting index
# after rearranging the array
def maxSum(n, a, l, q):

	# Stores elements after
	# rearranging
	v = []

	# Keeps track of visited
	# elements
	d = [0] * n

	# Traverse the queries
	for i in range(q):

		# Mark elements that are not
		# allowed to rearranged
		for x in range(l[i][0],
					l[i][1] + 1):

			if (d[x] == 0):
				d[x] = 1

	# Stores the indices
	st = set([])

	# Get indices and elements
	# that are allowed to rearranged
	for i in range(n):

		# Store the current index and
		# element
		if (d[i] == 0):
			v.append(a[i])
			st.add(i)

	# Sort vector v in descending
	# order
	v.sort(reverse = True)

	# Insert elements in array
	c = 0
	for it in st:
		a[it] = v
		c += 1

	# Stores the resultant sum
	pref_sum = 0

	# Stores the prefix sums
	temp_sum = 0

	# Traverse the given array
	for i in range(n):
		temp_sum += a[i]
		pref_sum += temp_sum

	# Return the maximum sum
	return pref_sum

# Driver Code
if __name__ == "__main__":

	# Given array
	arr = [-8, 4, -2,
		-6, 4, 7, 1]

	# Given size
	N = len(arr)

	# Queries
	q = [[0, 0], [4, 5]]

	# Number of queries
	queries = len(q)

	# Function Call
	print(maxSum(N, arr, q, queries))
