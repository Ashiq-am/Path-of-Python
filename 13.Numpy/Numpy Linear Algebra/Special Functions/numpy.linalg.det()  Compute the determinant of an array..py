# Python Program illustrating
# numpy.linalg.det() method

import numpy as np

# creating an array using
# array method
A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])

print(("\nDeterminant of A:"
       , np.linalg.det(A)))