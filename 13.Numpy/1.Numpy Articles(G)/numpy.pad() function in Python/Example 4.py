# Python program to explain
# working of numpy.pad() function
import numpy as np


arr = [[1, 3],[5, 8]]

# padding array using 'minimum' mode
pad_arr = np.pad(arr, (3,), 'minimum')

print(pad_arr)
