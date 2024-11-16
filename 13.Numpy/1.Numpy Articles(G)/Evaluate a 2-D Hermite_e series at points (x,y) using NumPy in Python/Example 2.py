# import packages
import numpy as np
from numpy.polynomial import hermite as H

# array of coefficients
array = np.array([[5,6],[7,8]])
print(array)

# shape of the array is
print("Shape of the array is : ",array.shape)

# dimension of the array
print("The dimension of the array is : ",array.ndim)

# Datatype of the array
print("Datatype of our Array is : ",array.dtype)

# evaluating a 2-d hermite series at point(x,y)
print(H.hermval2d(1,2,array))
