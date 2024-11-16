def minimum_cost(S, A, N):
	# size of string
	sze_of_S = len(S)

	# DP array initialized with infinity
	dp = [float('inf')] * (sze_of_S + 1)

	# base case
	dp[sze_of_S] = 0

	# size of string
	for i in range(sze_of_S - 1, -1, -1):
		# if we don't delete i'th character
		dp[i] = dp[i + 1] + 1

		# iterate over possible substrings that
		# can be removed from S
		for pos_substr_to_delete in A:
			# if substring from i'th character is equal to
			# e update the dp array by deleting this
			# substring
			if (
				i + len(pos_substr_to_delete) <= sze_of_S
				and S[i:i + len(pos_substr_to_delete)] == pos_substr_to_delete
			):
				dp[i] = min(dp[i], dp[i + len(pos_substr_to_delete)])

	# Returning answer
	return dp[0]


# Driver Code
if __name__ == "__main__":
	# Input
	S1 = "geeksforgeeks"
	N1 = 2
	A1 = ["geek", "for"]

	# Function Call
	print(minimum_cost(S1, A1, N1))
