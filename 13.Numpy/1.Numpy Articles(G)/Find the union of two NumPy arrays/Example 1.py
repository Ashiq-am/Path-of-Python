# import libraries
import numpy as np


arr1 = np.array([10, 20, 30, 40])
print("array1 ", arr1)

arr2 = np.array([20, 40, 60, 80])
print("array2 ", arr2)

# print union of the two arrays
print("Union of two arrays :", np.union1d(arr1, arr2))
