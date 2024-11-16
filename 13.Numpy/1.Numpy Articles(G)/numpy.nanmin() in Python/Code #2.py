# Python Program illustrating
# numpy.nanmin() method

import numpy as np

# 2D array
arr = [[np.nan, 17, 12, 33, 44],
       [15, 6, 27, 8, 19]]
print("\narr : \n", arr)

# Minimum of the flattened array
print("\nMin of arr, axis = None : ", np.nanmin(arr))

# Minimum along the first axis
# axis 0 means vertical
print("Min of arr, axis = 0 : ", np.nanmin(arr, axis=0))

# Minimum along the second axis
# axis 1 means horizontal
print("Min of arr, axis = 1 : ", np.nanmin(arr, axis=1))
