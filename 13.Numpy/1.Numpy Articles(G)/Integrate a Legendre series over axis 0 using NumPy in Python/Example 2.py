# import packages
import numpy as np
from numpy.polynomial import legendre as L

# array of coefficients
array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(array1)

# shape of the array is
print("Shape of array1 is: ", array1.shape)

# dimension of the array
print("The dimension of array1 is: ", array1.ndim)

# datatype of the array
print("Datatype of Array1 is: ", array1.dtype)

# adding two hermite series
print('Integrating the legendre series : ')
print(L.legint(array1,axis=1))
