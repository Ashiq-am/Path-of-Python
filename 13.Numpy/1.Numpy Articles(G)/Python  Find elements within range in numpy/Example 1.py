# python code to demonstrate
# finding elements in range
# in numpy array
import numpy as np

ini_array = np.array([1, 2, 3, 45, 4, 7, 810, 9, 6])

# printing initial array
print("initial_array : ", str(ini_array));

# find elements in range 6 to 10
result = np.where(np.logical_and(ini_array>= 6, ini_array<= 10))

# printing result
print("resultant_array : ", result)
