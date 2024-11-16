# Python Program illustrating
# numpy.mean() method
import numpy as np

# 2D array
arr = [[14, 17, 12, 33, 44],
       [15, 6, 27, 8, 19],
       [23, 2, 54, 1, 4, ]]

# mean of the flattened array
print("\nmean of arr, axis = None : ", np.mean(arr))

# mean along the axis = 0
print("\nmean of arr, axis = 0 : ", np.mean(arr, axis=0))

# mean along the axis = 1
print("\nmean of arr, axis = 1 : ", np.mean(arr, axis=1))

out_arr = np.arange(3)
print("\nout_arr : ", out_arr)
print("mean of arr, axis = 1 : ",
      np.mean(arr, axis=1, out=out_arr))
