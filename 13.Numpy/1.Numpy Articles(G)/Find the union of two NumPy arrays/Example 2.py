# import libraries
import numpy as np


# 2-d array
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
print("array1 ")
print(arr1)

arr2 = np.array([0, 5, 10])
print("array2 ", arr2)

# print union of 2-d array and 1-d array
print("Union of two arrays", np.union1d(arr1, arr2))
