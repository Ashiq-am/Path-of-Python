# Importing libraries
import numpy as np

# Creating 3D array
arr = np.array([[[3, 4], [5, 6]], [[7, 8], [9, 0]]])
print("Original array:\n", arr)

# Flattening the array
flattened_array = np.ravel(arr)
print("New flattened array:\n", flattened_array)
