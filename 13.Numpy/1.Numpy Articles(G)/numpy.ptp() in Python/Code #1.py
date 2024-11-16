# Python Program illustrating
# numpy.ptp() method

import numpy as np

# 1D array
arr = [1, 2, 7, 20, np.nan]
print("arr : ", arr)
print("Range of arr : ", np.ptp(arr))

# 1D array
arr = [1, 2, 7, 10, 16]
print("arr : ", arr)
print("Range of arr : ", np.ptp(arr))
