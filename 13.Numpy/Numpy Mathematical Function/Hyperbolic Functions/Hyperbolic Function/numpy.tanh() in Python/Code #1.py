# Python3 program explaining
# tanh() function

import numpy as np
import math

in_array = [0, math.pi / 2, np.pi / 3, np.pi]
print ("Input array : \n", in_array)

tanh_Values = np.tanh(in_array)
print ("\nTangent Hyperbolic values : \n", tanh_Values)
