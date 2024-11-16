# Python Program illustrating
# numpy.std() method
import numpy as np

# 2D array
arr = [[2, 2, 2, 2, 2],
       [15, 6, 27, 8, 2],
       [23, 2, 54, 1, 2, ],
       [11, 44, 34, 7, 2]]

# std of the flattened array
print("\nstd of arr, axis = None : ", np.std(arr))

# std along the axis = 0
print("\nstd of arr, axis = 0 : ", np.std(arr, axis=0))

# std along the axis = 1
print("\nstd of arr, axis = 1 : ", np.std(arr, axis=1))
