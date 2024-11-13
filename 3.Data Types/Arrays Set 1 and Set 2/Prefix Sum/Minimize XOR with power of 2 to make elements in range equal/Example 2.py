# Python code to implement the approach

# Function to calculate minimum operation
def MinimumOperations(N, A, Q, query):

	# dp array where dp[i][j] stores
	# the number of setbits
	# in first i elements at j position
	dp = [[0 for i in range(32)]
		for j in range(N + 1)]
	for i in range(N):
		for j in range(32):
			if (A[i] & (1 << j)):
				dp[i + 1][j] = 1

	# Loop to build the prefix sum array
	for i in range(2, N + 1):
		for j in range(32):
			dp[i][j] = dp[i][j] + dp[i - 1][j]
	ans = []

	# Loop to solve the queries
	for i in range(Q):
		l = query[i][0]
		r = query[i][1]
		y = 0
		n = (r - l + 1)
		for j in range(32):

			# Number of setbits in r-l+1 elements
			# at jth position
			x = dp[r + 1][j] - dp[l][j]
			y += min(x, n - x)
		ans.append(y)
	return ans


# Driver code
A = [2, 3, 1, 7]
N = len(A)
query = [[0, 2]]

# Function call
v = MinimumOperations(N, A, 1, query)
for i in range(len(v)):
	print(v[i], end=" ")

# This code is contributed by Tapesh(tapeshdua420)
