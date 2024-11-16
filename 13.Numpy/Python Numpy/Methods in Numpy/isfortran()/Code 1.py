# Python program explaining
# isfortran() function
import numpy as np

in_array = np.array([[1, 2, 3], [4, 5, 6]], order='C')
print ("Input array : \n", in_array)

exp2_values = np.exp2(in_array)
print ("\nisfortran : ", np.isfortran(in_array))
