# Python Program illustrating
# numpy.quantile() method
import numpy as np

# 2D array
arr = [[14, 17, 12, 33, 44],
       [15, 6, 27, 8, 19],
       [23, 2, 54, 1, 4, ]]
print("\narr : \n", arr)

# quantile of the flattened array
print("\n50th quantile of arr, axis = None : ", np.quantile(arr, .50))
print("0th quantile of arr, axis = None : ", np.quantile(arr, 0))

# quantile along the axis = 0
print("\n50th quantile of arr, axis = 0 : ", np.quantile(arr, .25, axis=0))
print("0th quantile of arr, axis = 0 : ", np.quantile(arr, 0, axis=0))

# quantile along the axis = 1
print("\n50th quantile of arr, axis = 1 : ", np.quantile(arr, .50, axis=1))
print("0th quantile of arr, axis = 1 : ", np.quantile(arr, 0, axis=1))

print("\n0th quantile of arr, axis = 1 : \n",
      np.quantile(arr, .50, axis=1, keepdims=True))
print("\n0th quantile of arr, axis = 1 : \n",
      np.quantile(arr, 0, axis=1, keepdims=True))
