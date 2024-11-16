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

# replace nan with col means
res = np.where(np.isnan(ini_array), np.ma.array(ini_array,
			mask = np.isnan(ini_array)).mean(axis = 0), ini_array)

# printing final array
print ("final array", res)
