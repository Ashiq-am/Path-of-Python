# Importing libraries
import numpy as np
from numpy import linalg

# Creating a 4X4 matrix
matrix = np.array([[1, 0, 1, 8], [1, 2, 0, 3], [4, 6, 2, 6], [0, 3, 6, 4]])
print("Original 4-D matrix")
print(matrix)

# Output
print("Determinant of the 4-D matrix:")
print(np.linalg.det(matrix))
