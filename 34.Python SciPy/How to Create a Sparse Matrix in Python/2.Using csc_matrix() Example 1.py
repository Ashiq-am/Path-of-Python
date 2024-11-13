# Python program to create
# sparse matrix using csc_matrix()

# Import required package
import numpy as np
from scipy.sparse import csc_matrix

# Creating a 3 * 4 sparse matrix
sparseMatrix = csc_matrix((3, 4),
						dtype = np.int8).toarray()

# Print the sparse matrix
print(sparseMatrix)
