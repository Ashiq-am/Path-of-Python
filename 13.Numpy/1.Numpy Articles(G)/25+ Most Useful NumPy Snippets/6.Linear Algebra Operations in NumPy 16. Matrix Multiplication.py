import numpy as np

# Creating two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication using @ operator
C = A @ B
print("Matrix Multiplication (A @ B):\n", C)

# Alternatively using np.dot()
D = np.dot(A, B)
print("Matrix Multiplication (np.dot()):\n", D)