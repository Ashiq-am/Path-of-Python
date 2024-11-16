# Python program explaining
# around() function

import numpy as np

in_array = [1 ,4, 7, 9, 12]
print ("Input array : \n", in_array)

round_off_values = np.around(in_array)
print ("\nRounded values : \n", round_off_values)


in_array = [133 ,344, 437, 449, 12]
print ("\nInput array : \n", in_array)

round_off_values = np.around(in_array, decimals = -2)
print ("\nRounded values upto 2: \n", round_off_values)

in_array = [133 ,344, 437, 449, 12]
print ("\nInput array : \n", in_array)

round_off_values = np.around(in_array, decimals = -3)
print ("\nRounded values upto 3: \n", round_off_values)
