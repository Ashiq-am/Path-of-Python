# import packages
import numpy as np
from numpy.polynomial import hermite_e as H

# Creating an array
array = np.array([4,3,5])
print(array)

# shape of the array is
print("Shape of the array is: ", array.shape)

# dimension of the array
print("The dimension of the array is: ", array.ndim)

# datatype of the array
print("Datatype of our Array is: ", array.dtype)

# differenciating a hermite series and setting
# derivatives
print(H.hermeder(array,m=2))
