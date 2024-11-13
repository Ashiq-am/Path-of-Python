# Python 3 implementation
# of the above approach

# Function to calclate the minimum
# sum from either end of the arrays
# for the given queries


def calculateQuery(arr, N, query, M):

	# Traverse the query[] array
	for i in range(M):
		X = query[i]

		# Stores sum from start
		# and end of the array
		sum_start = 0
		sum_end = 0

		# Calculate distance from start
		for j in range(N):

			sum_start += arr[j]
			if (arr[j] == X):
				break

		# Calculate distance from end
		for j in range(N - 1, -1, -1):

			sum_end += arr[j]
			if (arr[j] == X):
				break
		print(min(sum_end, sum_start), end=" ")

# Driver Code
if __name__ == "__main__":

	arr = [2, 3, 6, 7, 4, 5, 30]
	queries = [6, 5]
	N = len(arr)
	M = len(queries)

	calculateQuery(arr, N, queries, M)
