# Python code to demonstrate
# to count the number of elements
# in numpy which are zero

import numpy as np

ini_array1 = np.array([1, 2, 3, 4, 5, 6, 0])
ini_array2 = np.array([0, 0, 0, 0, 0, 0])

# printing initial arrays
print("initial arrays", ini_array1)
print(ini_array2)

# code to find whether all elements are zero
countzero_in1 = np.count_nonzero(ini_array1)
countzero_in2 = np.count_nonzero(ini_array2)

# printing result
print("Number of non-zeroes in array1 : ", countzero_in1)
print("Number of non-zeroes in array2 : ", countzero_in2)
