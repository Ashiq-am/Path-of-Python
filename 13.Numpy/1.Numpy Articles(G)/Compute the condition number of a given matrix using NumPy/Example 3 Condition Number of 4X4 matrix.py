# Importing library
import numpy as np

# Creating a 4X4 matrix
matrix = np.array([[4, 1, 4, 2], [3, 1, 2, 0],
				[3, 5, 7 ,1], [0, 6, 8, 4]])

print("Original matrix:")
print(matrix)

# Output
result = np.linalg.cond(matrix)

print("Condition number of the matrix:")
print(result)
