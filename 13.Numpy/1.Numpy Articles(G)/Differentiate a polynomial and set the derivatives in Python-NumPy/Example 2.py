# import packages
import numpy as np
from numpy.polynomial import polynomial as P

# Creating an array of polynomial coefficients
array = np.array([[5,6,7]])
print(array)

# shape of the array is
print("Shape of the array is : ",array.shape)

# dimension of the array
print("The dimension of the array is : ",array.ndim)

# Datatype of the array
print("Datatype of our Array is : ",array.dtype)

# differentiating the polynomial along columns
print(P.polyder(array,m=2,axis=1))
