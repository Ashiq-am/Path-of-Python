# import packages
import numpy as np
from numpy.polynomial import legendre as L

# array of coefficients
array = np.array([[10,20],[30,40]])
print(array)

# shape of the array is
print("Shape of the array is : ",array.shape)

# dimension of the array
print("The dimension of the array is : ",array.ndim)

# differenciate Legendre series
print(L.legder(array,1,axis =1))
