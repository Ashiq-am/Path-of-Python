# Python code to implement the approach
# Function to solve q Queries
def solveQueries(N, Queries):
	# // Initialize vectors
	matrix = [0]*(N+2) # (N + 2);
	for i in range(0, len(matrix)):
		matrix[i] = [0] * (N+2)

	row = [0]*(N+2)
	for i in range(0, len(row)):
		row[i] = [0]*(N+2)

	col = [0]*(N+2)
	for i in range(0, len(col)):
		col[i] = [0]*(N+2)
		# // Traverse over the queries
	for i in range(0, len(Queries)):
		a = Queries[i][0]
		b = Queries[i][1]
		c = Queries[i][2]
		d = Queries[i][3]
		row[a][b] += 1
		row[b] -= 1
		col[a][d + 1] -= 1
		col[d + 1] += 1

	for i in range(0, N):
		for j in range(1, N):
			row[j][i] += row[j - 1][i]
			col[j][i] += col[j - 1][i]

	# // Traverse and update matrix vector
	for i in range(0, N):
		matrix[i][0] = row[i][0] + col[i][0]

	for i in range(1, N+1):
		for j in range(0, N):
			matrix[j][i] += (matrix[j][i - 1]+row[j][i]+col[j][i])

	res = [0]*(N)
	for i in range(0, len(res)):
		res[i] = [0]*N # new Array(N).fill(0);
	for i in range(0, N):
		for j in range(0, N):
			res[i][j] = matrix[i][j]
	return res

# // function to prlet resultant matri
def printAns(res):
	for i in range(0, len(res)):
		for j in range(0, len(res[0])):
			print(res[i][j],end=" ")
		print()

# Driver Code
N = 6
q = 6
Queries = [[4, 0, 5, 3], [0, 0, 3, 4], [1, 2, 1, 2],
		[1, 1, 2, 3], [0, 0, 3, 1], [1, 0, 2, 4]]
res = solveQueries(N, Queries)
printAns(res)

# This code is contributed by ksam24000
