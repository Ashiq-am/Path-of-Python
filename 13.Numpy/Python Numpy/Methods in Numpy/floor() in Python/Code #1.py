# Python program explaining
# floor() function

import numpy as np

in_array = [.5, 1.5, 2.5, 3.5, 4.5, 10.1]
print ("Input array : \n", in_array)

flooroff_values = np.floor(in_array)
print ("\nRounded values : \n", flooroff_values)


in_array = [.53, 1.54, .71]
print ("\nInput array : \n", in_array)

flooroff_values = np.floor(in_array)
print ("\nRounded values : \n", flooroff_values)

in_array = [.5538, 1.33354, .71445]
print ("\nInput array : \n", in_array)

flooroff_values = np.floor(in_array)
print ("\nRounded values : \n", flooroff_values)
