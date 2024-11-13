# Python program for the above approach

# Function to find the required matrix


def matrixBlockSum(mat, K):

	# Stores number of rows and columns
	n = len(mat)
	m = len(mat[0])

	# Traverse the matrix mat[][]
	# row-wise to calculate prefix row sum
	for i in range(n):
		k = 0
		for j in range(m):

			# Calculate Prefix Sum
			k += mat[i][j]
			mat[i][j] = (mat[i][j], k)

	# Declare the final matrix
	ans = []

	# Traverse the matrix row-wise
	# and fill valid indices ans[i][j]
	for i in range(n):

		# Stores required sum of block
		# for each cell in current row
		temp = []
		for j in range(m):

			# Fix the bounds
			# i-k >=0 and i+k < n
			# j-k > =0 and j+k < m
			mnr = max(0, i - K)
			mnc = max(0, j - K)
			mxr = min(n - 1, i + K)
			mxc = min(m - 1, j + K)
			ans1 = 0

			# Iterate in range [minimum row(mnr),
			# maximum row(mxr)] and store the sum of row k
			#print(mnr,mxr+1)
			for k in range(mnr, mxr+1):
				ans1 += (mat[k][mxc][1]-mat[k][mnc][1])+mat[k][mnc][0]

			# Append it to temp
			temp.append(ans1)

		# Append temp to final matrix
		ans.append(temp)

	# Print the matrix
	print(ans)


# Driver Code
if __name__ == "__main__":

	mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	K = 1
	matrixBlockSum(mat, K)
