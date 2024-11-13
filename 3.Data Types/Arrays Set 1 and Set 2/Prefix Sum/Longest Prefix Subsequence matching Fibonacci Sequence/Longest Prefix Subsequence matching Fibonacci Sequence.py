# Maximum Length of longest Common subsequence
def solve(N, A):
	# Create an array dp as B
	dp = [0] * (N + 1)
	dp[0] = 1
	dp[1] = 1
	for i in range(2, N + 1):
		dp[i] = dp[i - 1] + dp[i - 2]

	count = 0
	j = 0
	for i in range(N):
		# If elements are matched
		if A[i] == dp[j]:
			j += 1
			count += 1
		if j == len(dp):
			dp.append(dp[-1] + dp[-2])

	# Return the LCS length
	return count

# Driver code
if __name__ == "__main__":
	N = 6
	A = [1, 2, 3, 1, 2, 3]

	# Function call
	print(solve(N, A))
