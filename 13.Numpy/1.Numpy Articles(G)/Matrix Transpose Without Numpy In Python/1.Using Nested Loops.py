matrix = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]

rows = len(matrix)
cols = len(matrix[0])

transposed = [[0 for _ in range(rows)] for _ in range(cols)]

for i in range(rows):
	for j in range(cols):
		transposed[j][i] = matrix[i][j]

print("Original Matrix:")
for row in matrix:
	print(row)

print("\nTransposed Matrix:")
for row in transposed:
	print(row)
