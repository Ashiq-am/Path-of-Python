# Python program to explain
# working of numpy.pad() function
import numpy as np


arr = [1, 3, 2, 5, 4]

# padding array using 'linear_ramp' mode
pad_arr = np.pad(arr, (3, 2), 'linear_ramp',
				end_values=(-4, 5))

print(pad_arr)
