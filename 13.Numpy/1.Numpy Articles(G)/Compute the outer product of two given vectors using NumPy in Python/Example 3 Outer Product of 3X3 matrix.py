# Importing library
import numpy as np

# Creating two 3-D matrix
matrix1 = np.array([[2, 8, 2], [3, 4, 8], [0, 2, 1]])
matrix2 = np.array([[2, 1, 1], [0, 1, 0], [2, 3, 0]])
print("Original 3-D matrix:")
print(matrix1)
print(matrix2)

# Output
print("Outer Product of the two matrix is:")
result = np.outer(matrix1, matrix2)
print(result)
