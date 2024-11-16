# Python3 program explaining
# degrees() function
import numpy as np
import math

in_array = [0, math.pi / 2, np.pi / 3, np.pi]
print ("Radian values : \n", in_array)

degree_Values = np.degrees(in_array)
print ("\nDegree values : \n", degree_Values)
