# import packages
import numpy as np
from numpy.polynomial import hermite_e as H

# Creating an array
array = np.array([[4,2,5],[1,4,2]])
print(array)

# shape of the array is
print("Shape of the array is: ", array.shape)

# dimension of the array
print("The dimension of the array is: ", array.ndim)

# Datatype of the array
print("Datatype of our Array is: ", array.dtype)

# differentiating a hermite series
print(H.hermeder(array,axis=1,m=2))
