# python program for the above approach

# Function to count the total number
# of possible valid arrays
def totalValidArrays(a, b, N):

	# Make a 2D DP table
	dp = [[0 for _ in range(b[N - 1] + 1)] for _ in range(N + 1)]

	# Make a 2D prefix sum table
	pref = [[0 for _ in range(b[N - 1] + 1)] for _ in range(N + 1)]

	# Base Case
	dp[0][0] = 1

	# Initialize the prefix values
	for i in range(0, b[N - 1] + 1):
		pref[0][i] = 1

	# Iterate over the range and update
	# the dp table accordingly
	for i in range(1, N + 1):
		for j in range(a[i - 1], b[i - 1] + 1):
			dp[i][j] += pref[i - 1][j]

			# Add the dp values to the
			# prefix sum
			pref[i][j] += dp[i][j]

		# Update the prefix sum table
		for j in range(0, b[N - 1] + 1):
			if (j > 0):
				pref[i][j] += pref[i][j - 1]

	# Find the result count of
	# arrays formed
	ans = 0
	for i in range(a[N - 1], b[N - 1] + 1):
		ans += dp[N][i]

	# Return the total count of arrays
	return ans

# Driver Code
if __name__ == "__main__":

	A = [1, 1]
	B = [2, 3]
	N = len(A)

	print(totalValidArrays(A, B, N))

	# This code is contributed by rakeshsahni
