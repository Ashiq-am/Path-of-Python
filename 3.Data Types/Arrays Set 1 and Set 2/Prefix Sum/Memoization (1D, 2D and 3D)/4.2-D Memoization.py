# Python3 program to memoize
# recursive implementation of LCS problem

# Returns length of LCS for X[0..m-1], Y[0..n-1]
# memoization applied in recursive solution
def lcs(X, Y, m, n):

	global arr

	# base case
	if (m == 0 or n == 0):
		return 0

	# if the same state has already been
	# computed
	if (arr[m - 1][n - 1] != -1):
		return arr[m - 1][n - 1]

	# if equal, then we store the value of the
	# function call
	if (X[m - 1] == Y[n - 1]):

		# store it in arr to avoid further repetitive
		# work in future function calls
		arr[m - 1][n - 1] = 1 + lcs(X, Y, m - 1, n - 1)
		return arr[m - 1][n - 1]

	else:

		# store it in arr to avoid further repetitive
		# work in future function calls
		arr[m - 1][n - 1] = max(lcs(X, Y, m, n - 1),
								lcs(X, Y, m - 1, n))
		return arr[m - 1][n - 1]


# Driver code

arr = [[0]*1000]*1000

for i in range(0, 1000):
	for j in range(0, 1000):
		arr[i][j] = -1

X = "AGGTAB"
Y = "GXTXAYB"

m = len(X)
n = len(Y)

print("Length of LCS is ", lcs(X, Y, m, n))
