import numpy as np
from numba import njit

# NumPy element-wise function
def numpy_exp(a):
    return np.exp(a)

# Numba-optimized element-wise function
@njit
def numba_exp(a):
    return np.exp(a)

# Example usage
a = np.random.rand(1000000)

%timeit numpy_exp(a)  # Original NumPy code
%timeit numba_exp(a)  # Numba-optimized code
