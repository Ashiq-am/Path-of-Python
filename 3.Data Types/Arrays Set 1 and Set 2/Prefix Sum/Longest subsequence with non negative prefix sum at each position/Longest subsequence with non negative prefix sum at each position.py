# Python3 Program for the above approach

# Function to find the length of the
# longest subsequence with non negative
# prefix sum at each position
def longestSubsequence(arr, N):

	# Stores the maximum sum possible
	# if we include j elements till
	# the position i

	# Initialize dp array with -1
	dp = [[-1 for i in range(N + 1)] for i in range(N)]

	# Maximum subsequence sum by
	# including no elements till
	# position 'i'
	for i in range(N):
		dp[i][0] = 0

	# Maximum subsequence sum by
	# including first element at
	# first position
	dp[0][1] = arr[0] if arr[0] >= 0 else -1

	# Iterate over all the remaining
	# positions
	for i in range(1, N):

		for j in range(1, i + 2):

			# If the current element
			# is excluded
			if (dp[i - 1][j] != -1):
				dp[i][j] = max(dp[i][j], dp[i - 1][j])

			# If current element is
			# included and if total
			# sum is positive or not
			if (dp[i - 1][j - 1] >= 0 and dp[i - 1][j - 1] + arr[i] >= 0):

				dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + arr[i])

	ans = 0

	# Select the maximum j by which
	# a non negative prefix sum
	# subsequence can be obtained
	for j in range(N + 1):
		if (dp[N - 1][j] >= 0):
			ans = j

	# Print the answer
	print(ans)

# Driver Code


arr = [4, -4, 1, -3, 1, -3]
N = len(arr)
longestSubsequence(arr, N)

# This code is contributed by _saurabhy_jaiswal
