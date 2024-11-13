# Python 3 program for the above approach

# Function to perform the given queries
# in the given empty array of size N
def updateQuery(queries, N):

	# Stores the resultant array
	# and the difference array
	ans = [0] * (N + 2)
	res = [0] * (N + 2)

	q = len(queries)

	# Traverse the given queries
	for i in range(q):
		# Starting index
		l = queries[i][0]

		# Ending index
		r = queries[i][1]

		# Increment l-th index by 1
		ans[l] += 1

		# Decrease r-th index by 1
		ans[r + 1] -= 1

		# Decrease (r + 1)th index by
		# the length of each query
		res[r + 1] -= (r - l + 1)

	# Find the prefix sum of ans[]
	for i in range(1, N+1):
		ans[i] += ans[i - 1]

	# Find the final array
	for i in range(1, N+1):
		res[i] += res[i - 1] + ans[i]

	# Printing the modified array
	for i in range(1, N+1):
		print(res[i], end=" ")

	print("\n")

# Driver Code
if __name__ == '__main__':
	N = 7
	queries = [[1, 7], [3, 6], [4, 5]]

	updateQuery(queries, N)

# This code is contributed by Anvesh Govind Saxena
