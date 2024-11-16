import numpy as np
from numba import njit

# NumPy element-wise multiplication
def numpy_multiply(a, b):
    return a * b

# Numba-optimized element-wise multiplication
@njit
def numba_multiply(a, b):
    return a * b

# Example usage
a = np.arange(1000000)
b = np.arange(1000000)

%timeit numpy_multiply(a, b)  # Original NumPy code
%timeit numba_multiply(a, b)  # Numba-optimized code
