# importing the numpy package
# as np
import numpy as np


def determinant(mat):
    # calling the det() method
    det = np.linalg.det(mat)
    return round(det)


# Driver Code
# declaring the matrix
mat = [[1, 0, 2, -1],
       [3, 0, 0, 5],
       [2, 1, 4, -3],
       [1, 0, 5, 0]]

# Function call
print('Determinant of the matrix is:',determinant(mat))


