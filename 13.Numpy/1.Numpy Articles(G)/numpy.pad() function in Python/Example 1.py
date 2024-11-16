# Python program to explain
# working of numpy.pad() function
import numpy as np


arr = [1, 3, 2, 5, 4]

# padding array using CONSTANT mode
pad_arr = np.pad(arr, (3, 2), 'constant',
				constant_values=(6, 4))

print(pad_arr)
