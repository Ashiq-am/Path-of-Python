import numpy as np


ar1 = np.arange(9).reshape(3, 3)
ar2 = np.arange(10, 19).reshape(3, 3)

# Original Higher dimension
print(ar1)

print(ar2)
print("")
r = np.einsum("mk,kn", ar1, ar2)

# Einstein’s summation convention of
# the said arrays
print(r)
