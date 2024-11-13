# Python3 Program to implement
# the above approach

# Function to flip a submatrices
def manipulation(matrix, q):

	# Boundaries of the submatrix
	x1, y1, x2, y2 = q

	# Iterate over the submatrix
	for i in range(x1-1, x2):
		for j in range(y1-1, y2):

			# Check for 1 or 0
			# and flip accordingly
			if matrix[i][j]:
				matrix[i][j] = 0
			else:
				matrix[i][j] = 1

# Function to perform the queries
def queries_fxn(matrix, queries):
	for q in queries:
		manipulation(matrix, q)


# Driver Code
matrix = [[0, 1, 0], [1, 1, 0]]
queries = [[1, 1, 2, 3], 
		[1, 1, 1, 1],
		[1, 2, 2, 3]]

# Function call
queries_fxn(matrix, queries)
print(matrix)
