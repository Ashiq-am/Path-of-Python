# Python code to implement the approach

MOD = 1000000007

# Function to count all possible
# non decreasing arrays
def countNonDecreasingArrays(A, B, N):
	# Initializing dp table with value 0
	dp = [[0] * 3001 for _ in range(N + 1)]

	# Base case
	dp[0][0] = 1

	for i in range(N):
		# Copying previous value where prefix
		# sum cannot be performed to avoid
		# segmentation fault
		dp[i + 1][0] = dp[i][0]

		# Taking prefix sum and improving Naive
		# dp by factor of O(N)
		for j in range(1, 3001):
			dp[i + 1][j] = (dp[i + 1][j - 1] + dp[i][j]) % MOD

		# Values are only needed from A[i] to B[i]
		# lets make other values zero
		for j in range(A[i]):
			dp[i + 1][j] = 0

		for j in range(B[i] + 1, 3001):
			dp[i + 1][j] = 0

	ans = 0

	# Answer will be sum of all dp[N][k]
	# where k is from 0 to 3000
	for i in range(3001):
		ans += dp[N][i]

	print(ans % MOD)

# Input 1
A = [1, 1]
B = [2, 3]
N = len(A)

# Function Call
countNonDecreasingArrays(A, B, N)

# Input 2
A1 = [2, 2, 2]
B1 = [2, 2, 2]
N1 = len(A1)

# Function Call
countNonDecreasingArrays(A1, B1, N1)

# This code is contributed by lokesh.
