# Python code to demonstrate
# converting array of strings to array of floats
# using asarray

import numpy as np

# initialising array
ini_array = np.array(["1.1", "1.5", "2.7", "8.9"])

# printing initial array
print ("initial array", str(ini_array))

# conerting to array of floats
# using np.asarray
final_array = b = np.asarray(ini_array,
		dtype = np.float64, order ='C')

# printing final result
print ("final array", str(final_array))
