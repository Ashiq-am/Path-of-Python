import numpy as np


array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Original 1-d arrays
print(array1)
print(array2)
r = np.einsum("n,n", a, b)

# Einstein’s summation convention of
# the said arrays
print(r)
