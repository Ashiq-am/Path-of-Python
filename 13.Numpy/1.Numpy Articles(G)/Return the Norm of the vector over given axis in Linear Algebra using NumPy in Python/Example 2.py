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

# returning the norm of the matrix along axis 1
print(l.norm(array, axis=1))
