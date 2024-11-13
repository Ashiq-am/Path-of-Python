# Python program to multpliply
# csc and csr matrices using multiply()

# Import required libraries
import numpy as np
from scipy.sparse import csc_matrix

# Create csc matrix
row_A = np.array([0, 0, 1, 2 ])
col_A = np.array([0, 1, 0, 1])
data_A = np.array([4, 3, 8, 9])

cscMatrix = csc_matrix((data_A, (row_A, col_A)),
						shape = (3, 3))

# print csc matrix
print("csc matrix: \n", cscMatrix.toarray())

# Create csr matrix
row_B = np.array([0, 1, 1, 2 ])
col_B = np.array([0, 0, 1, 0])
data_B = np.array([7, 2, 5, 1])

csrMatrix_B = csc_matrix((data_B, (row_B, col_B)),
						shape = (3, 3))

# print csr matrix
print("csr matrix:\n", csrMatrix_B.toarray())

# Multiply csc matrix with csr matrix
sparseMatrix = cscMatrix_A.multiply(csrMatrix_B)

# print resultant matrix
print("Product csc with csr Matrix:\n",
	sparseMatrix.toarray() )

# Multiply csr matrix with csc matrix
sparseMatrix = csrMatrix_A.multiply(cscMatrix_B)

# print resultant matrix
print("Product csr with csc Matrix:\n",
	sparseMatrix.toarray() )
