# Python program explaining
# isscalar() function
import numpy as np

in_array = [1, 3, 5, 4]
print ("Input array : ", in_array)

isscalar_values = np.isscalar(in_array)
print ("\nIs scalar : ", isscalar_values)

# input
print ("\nisscalar(7) : ", np.isscalar(7))

# list input
print ("\nisscalar([7]) : ", np.isscalar([7]))
