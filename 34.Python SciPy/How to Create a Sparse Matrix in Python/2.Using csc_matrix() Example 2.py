# Python program to create
# sparse matrix using csc_matrix()

# Import required package
import numpy as np
from scipy.sparse import csc_matrix

row = np.array([0, 0, 1, 1, 2, 1])
col = np.array([0, 1, 2, 0, 2, 2])

# taking data
data = np.array([1, 4, 5, 8, 9, 6])

# creating sparse matrix
sparseMatrix = csc_matrix((data, (row, col)),
						shape = (3, 3)).toarray()

# print the sparse matrix
print(sparseMatrix)
