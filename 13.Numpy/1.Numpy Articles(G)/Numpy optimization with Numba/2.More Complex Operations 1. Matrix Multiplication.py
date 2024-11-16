import numpy as np
from numba import njit

# NumPy matrix multiplication
def numpy_matrix_mult(a, b):
    return np.dot(a, b)

# Numba-optimized matrix multiplication
@njit
def numba_matrix_mult(a, b):
    return np.dot(a, b)

# Example usage
a = np.random.rand(1000, 1000)
b = np.random.rand(1000, 1000)

%timeit numpy_matrix_mult(a, b)  # Original NumPy code
%timeit numba_matrix_mult(a, b)  # Numba-optimized code
