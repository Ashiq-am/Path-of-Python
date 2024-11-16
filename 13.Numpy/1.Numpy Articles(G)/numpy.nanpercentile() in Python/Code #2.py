# Python Program illustrating
# numpy.nanpercentile() method

import numpy as np

# 2D array
arr = [[14, np.nan, 12, 33, 44],
       [15, np.nan, 27, 8, 19],
       [23, 2, np.nan, 1, 4, ]]
print("\narr : \n", arr)

# Percentile of the flattened array
print("\n50th Percentile of arr, axis = None : ",
      np.percentile(arr, 50))
print("\n50th Percentile of arr, axis = None : ",
      np.nanpercentile(arr, 50))
print("0th Percentile of arr, axis = None : ",
      np.nanpercentile(arr, 0))

# Percentile along the axis = 0
print("\n50th Percentile of arr, axis = 0 : ",
      np.nanpercentile(arr, 50, axis=0))
print("0th Percentile of arr, axis = 0 : ",
      np.nanpercentile(arr, 0, axis=0))

# Percentile along the axis = 1
print("\n50th Percentile of arr, axis = 1 : ",
      np.nanpercentile(arr, 50, axis=1))
print("0th Percentile of arr, axis = 1 : ",
      np.nanpercentile(arr, 0, axis=1))

print("\n0th Percentile of arr, axis = 1 : \n",
      np.nanpercentile(arr, 50, axis=1, keepdims=True))
print("\n0th Percentile of arr, axis = 1 : \n",
      np.nanpercentile(arr, 0, axis=1, keepdims=True))

