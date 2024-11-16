# Function to Minimum replacements to
# make array sorted containing only numbers 1, 2 and 3


def min_operations(arr, N):
	# DP array initialized with 0
	dp = [[0] * 4 for _ in range(N + 1)]

	# calculating answer till i'th element
	for i in range(1, N + 1):

		# i'th element is made 1 then (i - 1)th element
		# should be 1
		dp[i][1] = dp[i - 1][1] + (arr[i - 1] != 1)

		# i'th element is made 2 then (i- 1)th element
		# should be either 1 or 2
		dp[i][2] = min(dp[i - 1][1], dp[i - 1][2]) + (arr[i - 1] != 2)

		# if the i'th element is made 3 then (i - 1)th
		# element should be either 1, 2, or 3
		dp[i][3] = min(dp[i - 1][1], dp[i - 1][2],
					dp[i - 1][3]) + (arr[i - 1] != 3)

	# returning the final answer, the minimum number of operations
	# required to make the array sorted by replacing i'th
	# element by 1, 2, or 3
	return min(dp[N][1], dp[N][2], dp[N][3])


# Driver Code
if __name__ == "__main__":
	# Input
	N = 5
	arr = [2, 1, 3, 2, 1]

	# Function Call
	print(min_operations(arr, N))
