# Importing libraries
import numpy as np
from numpy import linalg

# Creating a 2X2 matrix
matrix = np.array([[1, 0], [3, 6]])
print("Original 2-D matrix")
print(matrix)

# Output
print("Determinant of the 2-D matrix:")
print(np.linalg.det(matrix))
