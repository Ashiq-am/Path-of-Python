# Python code to demonstrate
# to replace nan values
# with average of columns

import numpy as np

# Initialising numpy array
ini_array = np.array([[1.3, 2.5, 3.6, np.nan],
					[2.6, 3.3, np.nan, 5.5],
					[2.1, 3.2, 5.4, 6.5]])

# printing initial array
print ("initial array", ini_array)

# indices where values is nan in array
indices = np.where(np.isnan(ini_array))

# Iterating over numpy array to replace nan with values
for row, col in zip(*indices):
	ini_array[row, col] = np.mean(ini_array[
		~np.isnan(ini_array[:, col]), col])

# printing final array
print ("final array", ini_array)
