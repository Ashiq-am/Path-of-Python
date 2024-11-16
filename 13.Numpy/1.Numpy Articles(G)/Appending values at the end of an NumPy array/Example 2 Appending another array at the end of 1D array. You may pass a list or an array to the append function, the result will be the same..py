# importing the module
import numpy as np

# creating an array
arr1 = np.array([1, 2, 3])
print('First array is : ', arr1)

# creating another array
arr2 = np.array([4, 5, 6])
print('Second array is : ', arr2)

# appending arr2 to arr1
arr = np.append(arr1, arr2)
print('Array after appending : ', arr)
