# Importing libraries
import numpy as np

# Creating 2D array
arr = np.array([[5, 6, 7], [8, 9, 10]])
print("Original array:\n", arr)

# Flattening the array
flattened_array = np.ravel(arr)
print("New flattened array:\n", flattened_array)
