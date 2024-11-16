# Python code to demonstrate
# to replace negative values with 0
import numpy as np

ini_array1 = np.array([1, 2, -3, 4, -5, -6])

# printing initial arrays
print("initial array", ini_array1)

# Creating a array of 0
zero_array = np.zeros(ini_array1.shape, dtype=ini_array1.dtype)
print("Zero array", zero_array)

# code to replace all negative value with 0
ini_array2 = np.maximum(ini_array1, zero_array)

# printing result
print("New resulting array: ", ini_array2)
