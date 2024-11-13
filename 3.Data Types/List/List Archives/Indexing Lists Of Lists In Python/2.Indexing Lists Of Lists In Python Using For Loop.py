# Indexing using a for loop
rows = len(matrix)
columns = len(matrix[0])

print("\nUsing For Loop:")
for i in range(rows):
	for j in range(columns):
		print(f"Element at ({i}, {j}): {matrix[i][j]}")
