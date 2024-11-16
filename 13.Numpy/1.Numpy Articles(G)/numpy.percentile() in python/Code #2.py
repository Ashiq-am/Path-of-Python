# Python Program illustrating
# numpy.percentile() method

import numpy as np

# 2D array
arr = [[14, 17, 12, 33, 44],
       [15, 6, 27, 8, 19],
       [23, 2, 54, 1, 4, ]]
print("\narr : \n", arr)

# Percentile of the flattened array
print("\n50th Percentile of arr, axis = None : ",
      np.percentile(arr, 50))
print("0th Percentile of arr, axis = None : ",
      np.percentile(arr, 0))

# Percentile along the axis = 0
print("\n50th Percentile of arr, axis = 0 : ",
      np.percentile(arr, 50, axis=0))
print("0th Percentile of arr, axis = 0 : ",
      np.percentile(arr, 0, axis=0))
