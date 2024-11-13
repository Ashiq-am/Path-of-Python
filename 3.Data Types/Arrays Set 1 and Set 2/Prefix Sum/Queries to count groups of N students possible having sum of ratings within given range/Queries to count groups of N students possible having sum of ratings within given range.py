# Python3 program for the
# above approach

# Function to count number of
# ways to get given sum groups
def numWays(ratings, queries,
			n, k):

	# Initialise dp array
	dp = [[0 for i in range(10002)]
			for j in range(n)]

	# Mark all 1st row values as 1
	# since the mat[0][i] is all
	# possible sums in first row
	for i in range(k):
		dp[0][ratings[0][i]] += 1

	# Fix the ith row
	for i in range(1, n):

		# Fix the sum
		for sum in range(10001):

			# Iterate through all
			# values of ith row
			for j in range(k):

				# If sum can be obtained
				if (sum >= ratings[i][j]):
					dp[i][sum] += dp[i - 1][sum -
											ratings[i][j]]

	# Find the prefix sum of
	# last row
	for sum in range(1, 10001):
		dp[n - 1][sum] += dp[n - 1][sum - 1]

	# Traverse each query
	for q in range(len(queries)):
		a = queries[q][0]
		b = queries[q][1]

		# No of ways to form groups
		print(dp[n - 1][b] -
			dp[n - 1][a - 1],
			end = " ")

# Driver Code
if __name__ == '__main__':

	# Given N batches and
	# K students
	N = 2
	K = 3

	# Given ratings
	ratings = [[1, 2, 3],
			[4, 5, 6]]

	queries = [[6, 6],
			[1, 6]]

	# Function Call
	numWays(ratings, queries, N, K)


