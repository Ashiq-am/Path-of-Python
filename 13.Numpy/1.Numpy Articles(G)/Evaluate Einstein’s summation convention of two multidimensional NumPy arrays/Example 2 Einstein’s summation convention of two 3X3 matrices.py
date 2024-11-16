# Importing library
import numpy as np

# Creating two 3X3 matrix
matrix1 = np.array([[2, 3, 5], [4, 0, 2], [0, 6, 8]])
matrix2 = np.array([[0, 1, 5], [3, 4, 4], [8, 3, 0]])

print("Original matrix:")
print(matrix1)
print(matrix2)

# Output
result = np.einsum("mk,kn", matrix1, matrix2)

print("Einstein’s summation convention of the two matrix:")
print(result)
