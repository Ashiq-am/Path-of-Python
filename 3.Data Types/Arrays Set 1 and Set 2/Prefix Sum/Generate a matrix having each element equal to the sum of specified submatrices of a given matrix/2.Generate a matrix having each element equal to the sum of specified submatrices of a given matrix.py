# Python program for the above approach

# Function to generate the required matrix


def matrixBlockSum(mat, K):

		# Stores count of rows and columns
	n = len(mat)
	m = len(mat[0])

	# Traverse the matrix to
	# to compute prefix sum
	for i in range(n):

		for j in range(m):

			if i-1 >= 0:
				mat[i][j] += mat[i-1][j]
			if j-1 >= 0:
				mat[i][j] += mat[i][j-1]
			if i-1 >= 0 and j-1 >= 0:
				mat[i][j] -= mat[i-1][j-1]

	ans = [[0 for i in range(m)]for i in range(n)]

	# Traverse the matrix row-wise
	# to fill the required matrix
	for i in range(n):
		for j in range(m):

			# Fix the boundaries
			# i-k >=0 and i+k < n
			# j-k > =0 and j+k < m
			mnr = max(0, i - K)
			mxr = min(i + K, n-1)
			mnc = max(0, j - K)
			mxc = min(j + K, m-1)

			# Add sum of elements between
			# (0, 0) and (mxr, mxc)
			ans[i][j] = mat[mxr][mxc]

			# Remove elements between
			# (0, 0) and (mnr-1, mxc)
			if mnr - 1 >= 0:
				ans[i][j] -= mat[mnr-1][mxc]

			# Remove elements between
			# (0, 0) and (mxr, mnc-1)
			if mnc - 1 >= 0:
				ans[i][j] -= mat[mxr][mnc-1]

			# Add aux[mnr-1][mnc-1] as
			# elements between (0, 0)
				# and (mnr-1, mnc-1) are
			# subtracted twice
			if mnr - 1 >= 0 and mnc - 1 >= 0:
				ans[i][j] += mat[mnr - 1][mnc - 1]

	# Print the matrix
	print(ans)


# Driver Code
if __name__ == "__main__":

	mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

	K = 1

	matrixBlockSum(mat, K)
