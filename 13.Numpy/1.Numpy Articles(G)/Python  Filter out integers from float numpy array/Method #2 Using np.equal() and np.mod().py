# Python code to demonstrate
# filtering integers from numpy array
# containing integers and float

import numpy as np

# initialising array
ini_array = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0])

# printing initial array
print ("initial array : ", str(ini_array))

# filtering integers
result = ini_array[~np.equal(np.mod(ini_array, 1), 0)]

# printing resultant
print ("final array : ", str(result))
