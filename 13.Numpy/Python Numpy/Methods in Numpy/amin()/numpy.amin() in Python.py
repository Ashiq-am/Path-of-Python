# Python Program illustrating
# numpy.amin() method

import numpy as geek

# 1D array
arr = geek.arange(8)
print("arr : ", arr)
print("Min of arr : ", geek.amin(arr))

# 2D array
arr = geek.arange(10).reshape(2, 5)
print("\narr : ", arr)

# Minimum of the flattened array
print("\nMin of arr, axis = None : ", geek.amin(arr))

# Minimum along the first axis
# axis 0 means vertical
print("Min of arr, axis = 0 : ", geek.amin(arr, axis = 0))

# Minimum along the second axis
# axis 1 means horizontal
print("Min of arr, axis = 1 : ", geek.amin(arr, axis = 1))
