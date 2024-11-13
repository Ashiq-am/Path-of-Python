import numpy as np
from scipy.linalg import lstsq

# Example data
A = np.array([[1, 1], [1, 2], [1, 3]])
b = np.array([1, 2, 3])

# Solve least-squares problem
x, residuals, rank, s = lstsq(A, b)

print("Solution:", x)
print("Residuals:", residuals)
