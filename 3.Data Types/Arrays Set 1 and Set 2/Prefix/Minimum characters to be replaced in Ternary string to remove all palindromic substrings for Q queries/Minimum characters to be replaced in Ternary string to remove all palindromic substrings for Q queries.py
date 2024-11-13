# Python 3 program for the above approach
import sys
SIZE = 100005

# Function to preprocess the cost of
# converting the first j character to
# each sequence prefix[i]
def preprocess(s, t,
			prefix,
			n, i):

	# Initialize DP array
	prefix[i][0] = (s[0] != t[0])

	for j in range(1, n):

		# prefix[i][j] defines minimum
		# operations to transform first j
		# characters of s into sequence i
		prefix[i][j] = prefix[i][j - 1] + (s[j] != t[j % 3])
	return

# Function to find the minimum number of
# changes required to make each substring
# between [L, R] non-palindromic
def minChangesNonPalindrome(
		st, N, Q,
		queries):

	# Initialize the DP array
	prefix = [[0 for x in range(SIZE)]for y in range(6)]

	# Initialize the 6 different patterns
	# that can be formed to make substrings
	# non palindromic
	sequences = ["012", "021", "102",
				"120", "201", "210"]

	for i in range(6):

		# Preprocess the string with
		# the ith sequence
		preprocess(st, sequences[i],
				prefix, N, i)

	# Iterate through queries
	for i in range(Q):

		l = queries[i][0] + 1
		r = queries[i][1] + 1
		cost = sys.maxsize-1

		# Find the minimum operations by
		# comparing 6 different patterns
		# of the substrings
		for j in range(6):

			# Find the cost
			cost = min(cost, prefix[j][r] - prefix[j][l]
					+ (st[l] != sequences[j][l % 3]))

		print(cost)

# Driver Code
if __name__ == "__main__":

	S = "0200011011"
	queries = [[0, 4], [1, 6], [2, 8]]
	N = len(S)
	Q = len(queries)

	minChangesNonPalindrome(
		S, N, Q, queries)

	# This code is contributed by ukasp.
