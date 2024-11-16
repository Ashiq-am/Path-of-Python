# import packages
import numpy as np
from numpy.polynomial import chebyshev

# Creating an array
array = np.array([3,1,4])
print(array)

# shape of the array is
print("Shape of the array is : ",array.shape)

# dimension of the array
print("The dimension of the array is : ",array.ndim)

# Datatype of the array
print("Datatype of our Array is : ",array.dtype)

# raising chebyshev series to the power 2
print(chebyshev.chebpow(array,2))
