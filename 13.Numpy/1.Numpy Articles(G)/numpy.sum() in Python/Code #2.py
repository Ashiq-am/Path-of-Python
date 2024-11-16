# Python Program illustrating
# numpy.sum() method
import numpy as np

# 2D array
arr = [[14, 17, 12, 33, 44],
       [15, 6, 27, 8, 19],
       [23, 2, 54, 1, 4, ]]

print("\nSum of arr : ", np.sum(arr))

print("Sum of arr(uint8) : ", np.sum(arr, dtype=np.uint8))
print("Sum of arr(float32) : ", np.sum(arr, dtype=np.float32))

print("\nIs np.sum(arr).dtype == np.uint : ",
      np.sum(arr).dtype == np.uint)

print("Is np.sum(arr).dtype == np.uint : ",
      np.sum(arr).dtype == np.float)
