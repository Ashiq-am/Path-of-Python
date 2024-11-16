# Python program explaining
# expm1() function

import numpy as np

in_array = [1, 3, 5]
print ("Input array : \n", in_array)

exp_values = np.exp(in_array)
print ("\nExponential value of array element : "
	"\n", exp_values)

expm1_values = np.expm1(in_array)
print ("\n(Exponential value of array element) - (1) "
	": \n", expm1_values)
