# import packages
import numpy as np

# Creating an array
array = np.array([1,2,3])
print(array)

# shape of the array is
print("Shape of the array is : ",array.shape)

# dimension of the array
print("The dimension of the array is : ",array.ndim)

# Datatype of the array
print("Datatype of our Array is : ",array.dtype)

# computing power of input values
print(np.lib.scimath.power(array,2))
