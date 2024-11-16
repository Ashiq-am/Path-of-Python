# import packages
import numpy as np
from numpy.polynomial import chebyshev

# array of coefficients
c = np.array([1,2,3,4,5])
print(c)

# shape of the array is
print("Shape of the array is : ",c.shape)

# dimension of the array
print("The dimension of the array is : ",c.ndim)

# Datatype of the array
print("Datatype of our Array is : ",c.dtype)

# return the scaled companion matrix of
# a 1-D array
print(chebyshev.chebcompanion(c))
