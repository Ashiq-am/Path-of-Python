# import packages
import numpy as np
from numpy.polynomial import hermite

# array of coefficients
c = np.array([2,2,3])
print(c)

# shape of the array is
print("Shape of the array is : ",c.shape)

# dimension of the array
print("The dimension of the array is : ",c.ndim)

# Datatype of the array
print("Datatype of our Array is : ",c.dtype)

#evaluating hermite series
print(hermite.hermgrid3d([1,2],[3,4],[5,6],c))
