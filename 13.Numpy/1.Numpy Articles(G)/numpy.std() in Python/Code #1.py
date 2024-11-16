# Python Program illustrating
# numpy.std() method
import numpy as np

# 1D array
arr = [20, 2, 7, 1, 34]

print("arr : ", arr)
print("std of arr : ", np.std(arr))

print("\nMore precision with float32")
print("std of arr : ", np.std(arr, dtype=np.float32))

print("\nMore accuracy with float64")
print("std of arr : ", np.std(arr, dtype=np.float64))
