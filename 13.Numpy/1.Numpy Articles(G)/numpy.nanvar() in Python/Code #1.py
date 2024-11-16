# Python Program illustrating
# numpy.nanvar() method
import numpy as np

# 1D array
arr = [20, 2, np.nan, 1, 34]

print("arr : ", arr)
print("\nnanvar of arr : ", np.nanvar(arr))

print("var of arr : ", np.var(arr))

print("\nnanvar of arr : ", np.nanvar(arr, dtype=np.float32))
print("var of arr : ", np.var(arr, dtype=np.float32))

