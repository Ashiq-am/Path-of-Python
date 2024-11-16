# Python3 program explaining
# sinc() function
import numpy as np
import math

in_array = [0, math.pi / 2, np.pi / 3, np.pi]
print ("Input array : \n", in_array)

sinc_Values = np.sinc(in_array)
print ("\nSinc values : \n", sinc_Values)
