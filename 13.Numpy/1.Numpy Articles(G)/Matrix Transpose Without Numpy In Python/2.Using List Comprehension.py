matrix = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print("Original Matrix:")
for row in matrix:
	print(row)

print("\nTransposed Matrix:")
for row in transposed:
	print(row)
