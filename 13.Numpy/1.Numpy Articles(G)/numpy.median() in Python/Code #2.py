# Python Program illustrating
# numpy.median() method
import numpy as np

# 2D array
arr = [[14, 17, 12, 33, 44],
       [15, 6, 27, 8, 19],
       [23, 2, 54, 1, 4, ]]

# median of the flattened array
print("\nmedian of arr, axis = None : ", np.median(arr))

# median along the axis = 0
print("\nmedian of arr, axis = 0 : ", np.median(arr, axis=0))

# median along the axis = 1
print("\nmedian of arr, axis = 1 : ", np.median(arr, axis=1))

out_arr = np.arange(3)
print("\nout_arr : ", out_arr)
print("median of arr, axis = 1 : ",
      np.median(arr, axis=1, out=out_arr))
