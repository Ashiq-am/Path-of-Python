# Python Program illustrating
# numpy.nanquantile() method

import numpy as np

# 2D array
arr = [[14, np.nan, 12, 33, 44],
       [15, np.nan, 27, 8, 19],
       [23, 2, np.nan, 1, 4, ]]
print("\narr : \n", arr)

# quantile of the flattened array
print("\nQ2 quantile of arr, axis = None : ", np.quantile(arr, .50))
print("\nQ2 quantile of arr, axis = None : ", np.nanquantile(arr, .50))
print("0th quantile of arr, axis = None : ", np.nanquantile(arr, 0))
