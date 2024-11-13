# A memoize recursive implementation of LCS problem

# Returns length of LCS for X[0..m-1], Y[0..n-1] */
# memoization applied in recursive solution
def lcs(X, Y, Z, m, n, o):
	global arr

	# base case
	if(m == 0 or n == 0 or o == 0):
		return 0

	# if the same state has already been
	# computed
	if (arr[m - 1][n - 1][o - 1] != -1):
		return arr[m - 1][n - 1][o - 1]

	# if equal, then we store the value of the
	# function call
	if (X[m - 1] == Y[n - 1] and
			Y[n - 1] == Z[o - 1]):

		# store it in arr to avoid further repetitive work
		# in future function calls
		arr[m - 1][n - 1][o - 1] = 1 + lcs(X, Y, Z, m - 1,
										n - 1, o - 1)
		return arr[m - 1][n - 1][o - 1]

	else:

		# store it in arr to avoid further repetitive work
		# in future function calls
		arr[m - 1][n - 1][o - 1] = max(lcs(X, Y, Z, m, n - 1, o),
									max(lcs(X, Y, Z, m - 1, n, o), lcs(X, Y, Z, m, n, o - 1)))
		return arr[m - 1][n - 1][o - 1]

# Driver Code
arr = [[[0 for k in range(100)] for j in range(100)] for i in range(100)]

for i in range(100):
	for j in range(100):
		for k in range(100):
			arr[i][j][k] = -1

X = "geeks"
Y = "geeksfor"
Z = "geeksforgeeks"
m = len(X)
n = len(Y)
o = len(Z)
print("Length of LCS is ", lcs(X, Y, Z, m, n, o))
