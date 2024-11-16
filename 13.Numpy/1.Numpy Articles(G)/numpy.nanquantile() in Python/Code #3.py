# Python Program illustrating
# numpy.nanquantile() method
import numpy as np

# 2D array
arr = [[14, np.nan, 12, 33, 44],
       [15, np.nan, 27, 8, 19],
       [23, 2, np.nan, 1, 4, ]]
print("\narr : \n", arr)

# quantile along the axis = 0
print("\nQ2 quantile of arr, axis = 0 : ", np.nanquantile(arr, .50, axis=0))
print("0th quantile of arr, axis = 0 : ", np.nanquantile(arr, 0, axis=0))

# quantile along the axis = 1
print("\nQ2 quantile of arr, axis = 1 : ", np.nanquantile(arr, .50, axis=1))
print("0th quantile of arr, axis = 1 : ", np.nanquantile(arr, 0, axis=1))

print("\nQ2 quantile of arr, axis = 1 : \n",
      np.nanquantile(arr, .50, axis=1, keepdims=True))
print("\n0th quantile of arr, axis = 1 : \n",
      np.nanquantile(arr, 0, axis=1, keepdims=True))
