# import packages
import numpy.linalg as l
import numpy as np

# Creating an array
array = np.arange(12).reshape((3, 4))
print(array)

# shape of the array is
print("Shape of the array is : ", array.shape)

# dimension of the array
print("The dimension of the array is : ", array.ndim)

# Datatype of the array
print("Datatype of our Array is : ", array.dtype)

# returning the infinity norm of the matrix
print(l.norm(array, np.inf))
