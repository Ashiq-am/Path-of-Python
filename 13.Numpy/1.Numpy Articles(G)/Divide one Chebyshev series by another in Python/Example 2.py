# import packages
import numpy as np
from numpy.polynomial import chebyshev as Chev

# Creating arrays of coefficients
# neither quotient and remainder "intuitive"
array = np.array([11, 22, 33])
array2 = np.array([1, 11, 22, 33])
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
print(Chev.chebdiv(array2, array))
