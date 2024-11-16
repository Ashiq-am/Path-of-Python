# importing packages
import numpy as np
from numpy.polynomial import legendre as L

# array of coefficients
array = np.array([[[40,30],[12,15]]])
print(array)

# shape of the array is
print("Shape of the array is : ",array.shape)

# dimension of the array
print("The dimension of the array is : ",array.ndim)

# Datatype of the array
print("Datatype of our Array is : ",array.dtype)

# evaluating a 3D languerre series
print(L.legval3d([1.3,3],[2,3.5],[2,3],array))
