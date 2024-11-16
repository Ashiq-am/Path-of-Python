import numpy as np

# Example 2D array
matrix = np.array([
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
])

# List comprehension for slicing
result = [row[1:3] for row in matrix[0:2]]
print(type(matrix))
print(result)
