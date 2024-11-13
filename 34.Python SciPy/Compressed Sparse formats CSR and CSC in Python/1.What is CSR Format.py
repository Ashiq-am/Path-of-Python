import numpy as np
from scipy.sparse import csr_matrix
# Example sparse matrix
matrix = np.array([[0, 0, 1],
                   [4, 0, 0],
                   [0, 0, 3]])
# Create a CSR matrix
csr = csr_matrix(matrix)
# Display the CSR matrix
print("CSR matrix:")
print(csr)
# Components of CSR matrix
print("\nData:", csr.data)
print("Indices:", csr.indices)
print("Index pointer:", csr.indptr)
