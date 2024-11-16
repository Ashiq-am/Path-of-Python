# Python code to demonstrate
# finding elements in range
# in numpy array

import numpy as np

ini_array = np.array([1, 2, 3, 45, 4, 7, 9, 6])

# printing initial array
print("initial_array : ", str(ini_array));


# find elements in range 6 to 10
result = ini_array[(ini_array>6)*(ini_array<10)]

# printing result
print("resultant_array : ", result)
