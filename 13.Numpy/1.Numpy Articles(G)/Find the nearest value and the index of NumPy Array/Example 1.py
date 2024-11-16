import numpy as np


# array
arr = np.array([8, 7, 1, 5, 3, 4])
print("Array is : ", arr)

# element to which nearest value is to be found
x = 2
print("Value to which nearest element is to be found: ", x)

# calculate the difference array
difference_array = np.absolute(arr-x)

# find the index of minimum element from the array
index = difference_array.argmin()
print("Nearest element to the given values is : ", arr[index])
print("Index of nearest value is : ", index)
