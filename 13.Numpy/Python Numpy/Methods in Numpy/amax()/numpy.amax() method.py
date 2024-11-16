# Python Program illustrating
# numpy.amax() method

import numpy as geek

# 1D array
arr = geek.arange(8)
print("arr : ", arr)
print("Max of arr : ", geek.amax(arr))

# 2D array
arr = geek.arange(10).reshape(2, 5)
print("\narr : ", arr)

# Maximum of the flattened array
print("\nMax of arr, axis = None : ", geek.amax(arr))

# Maxima along the first axis
# axis 0 means vertical
print("Max of arr, axis = 0 : ", geek.amax(arr, axis = 0))

# Maxima along the second axis
# axis 1 means horizontal
print("Max of arr, axis = 1 : ", geek.amax(arr, axis = 1))
