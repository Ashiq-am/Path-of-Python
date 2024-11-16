# Python code to demonstrate
# filtering integers from numpy array
# containing integers and float

import numpy as np

# initialising array
ini_array = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0])

# printing initial array
print ("initial array : ", str(ini_array))

# filtering integers
mask = np.isclose(ini_array, ini_array.astype(int))
result = ini_array[~mask]

# printing resultant
print ("final array : ", str(result))
