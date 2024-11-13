# Python program to multpliply two
# csr matrices using multiply()

# Import required libraries
import numpy as np
from scipy.sparse import csr_matrix

# Create first csr matrix A
row_A = np.array([0, 0, 1, 2 ])
col_A = np.array([0, 1, 0, 1])
data_A = np.array([4, 3, 8, 9])

csrMatrix_A = csr_matrix((data_A, (row_A, col_A)),
						shape = (3, 3))

# print first csr matrix
print("first csr matrix: \n", csrMatrix_A.toarray())

# Create second csr matrix B
row_B = np.array([0, 1, 1, 2 ])
col_B = np.array([0, 0, 1, 0])
data_B = np.array([7, 2, 5, 1])

csrMatrix_B = csr_matrix((data_B, (row_B, col_B)),
						shape = (3, 3))

# print second scr matrix
print("second csr matrix:\n", csrMatrix_B.toarray())

# Multiply these matrices
sparseMatrix_AB = csrMatrix_A.multiply(csrMatrix_B)

# print resultant matrix
print("Product Sparse Matrix:\n",sparseMatrix_AB.toarray() )
