# Python Program illustrating
# numpy.var() method
import numpy as np

# 2D array
arr = [[2, 2, 2, 2, 2],
       [15, 6, 27, 8, 2],
       [23, 2, 54, 1, 2, ],
       [11, 44, 34, 7, 2]]

# var of the flattened array
print("\nvar of arr, axis = None : ", np.var(arr))

# var along the axis = 0
print("\nvar of arr, axis = 0 : ", np.var(arr, axis=0))

# var along the axis = 1
print("\nvar of arr, axis = 1 : ", np.var(arr, axis=1))
