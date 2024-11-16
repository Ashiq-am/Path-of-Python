# import packages
import numpy as np
from numpy.polynomial import chebyshev as Chev

# Creating arrays of coefficients
array = np.array([3, 1, 4])
array2 = np.array([5, 7, 9])
print(array)
print(array2)

# shape of the arrays
print("Shape of the array1 is : ", array.shape)
print("Shape of the array2 is : ", array2.shape)

# dimensions of the array
print("The dimension of the array1 is : ", array.ndim)
print("The dimension of the array2 is : ", array2.ndim)

# Datatype of the arrays
print("Datatype of our Array1 is : ", array.dtype)
print("Datatype of our Array2 is : ", array2.dtype)

# dividing Chebyshev series
print(Chev.chebdiv(array, array2))
