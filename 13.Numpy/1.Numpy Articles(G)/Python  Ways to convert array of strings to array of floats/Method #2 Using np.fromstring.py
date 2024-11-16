# Python code to demonstrate converting
# array of strings to array of floats
# using fromstring

import numpy as np

# initialising array
ini_array = np.array(["1.1", "1.5", "2.7", "8.9"])

# printing initial array
print ("initial array", str(ini_array))

# conerting to array of floats
# using np.fromstring
ini_array = ', '.join(ini_array)
ini_array = np.fromstring(ini_array, dtype = np.float,
										sep =', ' )

# printing final result
print ("final array", str(ini_array))
