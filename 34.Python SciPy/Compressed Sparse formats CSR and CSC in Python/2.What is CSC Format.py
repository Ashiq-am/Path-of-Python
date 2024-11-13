import numpy as np
from scipy.sparse import csc_matrix
# Example sparse matrix
matrix = np.array([[0, 0, 1],
                   [4, 0, 0],
                   [0, 0, 3]])
# Create a CSC matrix
csc = csc_matrix(matrix)
# Display the CSC matrix
print("CSC matrix:")
print(csc)
# Components of CSC matrix
print("\nData:", csc.data)
print("Indices:", csc.indices)
print("Index pointer:", csc.indptr)
