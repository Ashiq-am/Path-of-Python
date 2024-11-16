import numpy as np

# 2D array
arr = [[np.nan, 17, 12, 33, 44],
       [15, 6, 27, 8, 19]]
print("\narr : \n", arr)

# maximum of the flattened array
print("\nmax of arr, axis = None : ", np.nanmax(arr))

# maximum along the first axis
# axis 0 means vertical
print("max of arr, axis = 0 : ", np.nanmax(arr, axis=0))

# maximum along the second axis
# axis 1 means horizontal
print("max of arr, axis = 1 : ", np.nanmax(arr, axis=1))
