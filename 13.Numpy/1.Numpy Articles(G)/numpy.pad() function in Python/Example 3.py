# Python program to explain
# working of numpy.pad() function
import numpy as np


arr = [1, 3, 9, 5, 4]

# padding array using 'maximum' mode
pad_arr = np.pad(arr, (3,), 'maximum')

print(pad_arr)
