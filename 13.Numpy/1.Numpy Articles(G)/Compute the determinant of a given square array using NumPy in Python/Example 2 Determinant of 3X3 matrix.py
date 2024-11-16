# Importing libraries
import numpy as np
from numpy import linalg

# Creating a 3X3 matrix
matrix = np.array([[1, 0, 1], [1, 2, 0], [4, 6, 2]])
print("Original 3-D matrix")
print(matrix)

# Output
print("Determinant of the 3-D matrix:")
print(np.linalg.det(matrix))
