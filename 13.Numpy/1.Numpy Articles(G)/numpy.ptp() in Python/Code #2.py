# Python Program illustrating
# numpy.ptp() method

import numpy as np

# 3D array
arr = [[14, 17, 12, 33, 44],
       [15, 6, 27, 8, 19],
       [23, 2, 54, 1, 4, ]]
print("\narr : \n", arr)

# Range of the flattened array
print("\nRange of arr, axis = None : ", np.ptp(arr))

# Range along the first axis
# axis 0 means vertical
print("Range of arr, axis = 0 : ", np.ptp(arr, axis=0))

# Range along the second axis
# axis 1 means horizontal
print("Min of arr, axis = 1 : ", np.ptp(arr, axis=1))
