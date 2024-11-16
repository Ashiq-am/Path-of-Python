# python code to demonstrate
# adding columns in numpy array

import numpy as np

ini_array = np.array([[1, 2, 3], [45, 4, 7], [9, 6, 10]])

# printing initial array
print("initial_array : ", str(ini_array));

# Array to be added as column
column_to_be_added = np.array([1, 2, 3])

# Adding column to numpy array
result = np.column_stack((ini_array, column_to_be_added))

# printing result
print ("resultant array", str(result))
