# Python program explaining
# ceil() function
import numpy as np

in_array = [1.67, 4.5, 7, 9, 12]
print ("Input array : \n", in_array)

ceiloff_values = np.ceil(in_array)
print ("\nRounded values : \n", ceiloff_values)


in_array = [133.000, 344.54, 437.56, 44.9, 1.2]
print ("\nInput array : \n", in_array)

ceiloff_values = np.ceil(in_array)
print ("\nRounded values upto 2: \n", ceiloff_values)
