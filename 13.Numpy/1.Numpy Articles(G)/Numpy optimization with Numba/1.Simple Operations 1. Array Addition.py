import numpy as np
from numba import njit

# NumPy array addition
def numpy_add(a, b):
    return a + b

# Numba-optimized array addition
@njit
def numba_add(a, b):
    return a + b

# Example usage
a = np.arange(1000000)
b = np.arange(1000000)

%timeit numpy_add(a, b)  # Original NumPy code
%timeit numba_add(a, b)  # Numba-optimized code
