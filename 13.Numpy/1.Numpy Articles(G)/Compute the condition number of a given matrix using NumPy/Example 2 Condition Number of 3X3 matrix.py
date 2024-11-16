# Importing library
import numpy as np

# Creating a 3X3 matrix
matrix = np.array([[4, 2, 0], [3, 1, 2], [1, 6, 4]])

print("Original matrix:")
print(matrix)

# Output
result = np.linalg.cond(matrix)

print("Condition number of the matrix:")
print(result)
