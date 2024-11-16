# Python Program illustrating
# numpy.nanmax() method

import numpy as np

# 1D array
arr = [1, 2, 7, 0, np.nan]
print("arr : ", arr)
print("max of arr : ", np.amax(arr))

# nanmax ignores NaN values.
print("nanmax of arr : ", np.nanmax(arr))

