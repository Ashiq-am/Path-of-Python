# Python code to check that whether
# all elements in numpy are zero

import numpy as np

ini_array1 = np.array([1, 2, 3, 4, 5, 6, 0])
ini_array2 = np.array([0, 0, 0, 0, 0, 0])

# printing initial arrays
print("initial arrays", ini_array1)

# code to find whether all elements are zero
countzero_in1 = not np.any(ini_array1)
countzero_in2 = not np.any(ini_array2)

# printing result
print("Whole array contains zeroes in array1 ?: ", countzero_in1)
print("Whole array contains zeroes in array2 ?: ", countzero_in2)
