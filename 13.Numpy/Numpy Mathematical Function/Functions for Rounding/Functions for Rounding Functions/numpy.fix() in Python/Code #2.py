# Python program explaining
# fix() function

import numpy as np

in_array = [1, 4, 7, 9, 12]
print ("Input array : \n", in_array)

fixoff_values = np.fix(in_array)
print ("\nRounded values : \n", fixoff_values)


in_array = [133, 344, 437, 449, 12]
print ("\nInput array : \n", in_array)

fixoff_values = np.fix(in_array)
print ("\nRounded values upto 2: \n", fixoff_values)

in_array = [133, 344, 437, 449, 12]
print ("\nInput array : \n", in_array)

fixoff_values = np.fix(in_array)
print ("\nRounded values upto 3: \n", fixoff_values)
