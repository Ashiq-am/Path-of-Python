# Python Program illustrating
# numpy.nanvar() method
import numpy as np

# 2D array
arr = [[2, 2, 2, 2, 2],
       [15, 6, np.nan, 8, 2],
       [23, 2, 54, 1, 2, ],
       [np.nan, 44, 34, 7, 2]]

# nanvar of the flattened array
print("\nnanvar of arr, axis = None : ", np.nanvar(arr))

print("\nvar of arr, axis = None : ", np.var(arr))

# nanvar along the axis = 0
print("\nnanvar of arr, axis = 0 : \n", np.nanvar(arr, axis=0))

print("\nvar of arr, axis = 0 : ", np.var(arr, axis=0))

# nanvar along the axis = 1
print("\nnanvar of arr, axis = 1 : ", np.nanvar(arr, axis=1))
