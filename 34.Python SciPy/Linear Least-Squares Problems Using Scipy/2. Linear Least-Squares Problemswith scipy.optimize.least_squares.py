import numpy as np
from scipy.linalg import lstsq
from scipy.optimize import least_squares

# Define the data for least-squares problem
A = np.array([[1, 1], [1, 2], [1, 3]])
b = np.array([1, 2, 3])

# Solve least-squares problem using lstsq
x_lstsq, residuals, rank, s = lstsq(A, b)
print("Solution using lstsq:", x_lstsq)
print("Residuals using lstsq:", residuals)

# Define the residuals function for least_squares
def residuals_func(x):
    return np.dot(A, x) - b

# Initial guess for the solution
x0 = np.zeros(A.shape[1])

# Solve least-squares problem using least_squares
result = least_squares(residuals_func, x0)
print("Solution using least_squares:", result.x)
print("Residuals using least_squares:", result.fun)
