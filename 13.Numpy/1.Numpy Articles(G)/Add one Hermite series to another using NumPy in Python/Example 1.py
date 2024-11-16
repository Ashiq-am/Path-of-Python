# import packages
import numpy as np
from numpy.polynomial import hermite_e as H

# array1 coefficients
array1 = np.array([1,2,3,4,5])
print(array1)

# array2 coefficients
array2 = np.array([6,7,8,9,10])
print(array2)

# shape of the arrays are
print("Shape of array1 is: ", array1.shape)
print("Shape of array1 is: ", array2.shape)

# dimensions of the array
print("The dimension of array1 is: ", array1.ndim)
print("The dimension of array2 is: ", array2.ndim)

# adding two hermite series
print('addition of the two hermite series : ')
print(H.hermeadd(array1,array2))
