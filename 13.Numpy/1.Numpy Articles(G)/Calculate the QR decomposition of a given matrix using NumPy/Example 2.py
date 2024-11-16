import numpy as np


# Original matrix
matrix1 = np.array([[1, 0], [2, 4]])
print(matrix1)

# Decomposition of the said matrix
q, r = np.linalg.qr(matrix1)
print('\nQ:\n', q)
print('\nR:\n', r)
