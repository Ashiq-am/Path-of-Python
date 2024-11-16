# Importing library
import numpy as np

# Creating two 4X4 matrix
matrix1 = np.array([[1, 2, 3, 5], [4, 4, 0, 2],
					[0, 1, 6, 8], [0, 5, 6, 9]])

matrix2 = np.array([[0, 1, 9, 2], [3, 3, 4, 4],
					[1, 8, 3, 0], [5, 2, 1, 6]])

print("Original matrix:")
print(matrix1)
print(matrix2)

# Output
result = np.einsum("mk,kn", matrix1, matrix2)

print("Einstein’s summation convention of the two matrix:")
print(result)
