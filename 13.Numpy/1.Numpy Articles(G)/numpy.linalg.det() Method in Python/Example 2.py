import numpy as np
from numpy import linalg as LA


array1 = np.array([[1, 2, 3], [3, 4, 1], [3, 2, 1]])

# Original 2-d array
print(array1)

# Determinant of the said 2-D array
print(np.linalg.det(array1))
