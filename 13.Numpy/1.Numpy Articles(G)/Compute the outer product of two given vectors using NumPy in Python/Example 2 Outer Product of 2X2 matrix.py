# Importing library
import numpy as np

# Creating two 2-D matrix
matrix1 = np.array([[1, 3], [2, 6]])
matrix2 = np.array([[0, 1], [1, 9]])
print("Original 2-D matrix:")
print(matrix1)
print(matrix2)

# Output
print("Outer Product of the two matrix is:")
result = np.outer(matrix1, matrix2)
print(result)
