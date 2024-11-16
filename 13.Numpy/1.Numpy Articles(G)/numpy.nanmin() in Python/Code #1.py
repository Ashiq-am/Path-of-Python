# Python Program illustrating
# numpy.nanmin() method

import numpy as np

# 1D array
arr = [1, 2, 7, 0, np.nan]
print("arr : ", arr)
print("Min of arr : ", np.amin(arr))

# nanmin ignores NaN values.
print("nanMin of arr : ", np.nanmin(arr))
