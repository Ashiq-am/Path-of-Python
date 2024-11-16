# Python program explaining
# trunc() function

import numpy as np

in_array = [1.67, 4.5, 7, 9, 12]
print ("Input array : \n", in_array)

truncoff_values = np.trunc(in_array)
print ("\nRounded values : \n", truncoff_values)


in_array = [133.000, 344.54, 437.56, 44.9, 1.2]
print ("\nInput array : \n", in_array)

truncoff_values = np.trunc(in_array)
print ("\nRounded values upto 2: \n", truncoff_values)
