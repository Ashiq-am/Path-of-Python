# import packages
import numpy as np

# Creating an array
array = np.array([10,20,30])
print(array)

# shape of the array is
print("Shape of the array is : ",array.shape)

# dimension of the array
print("The dimension of the array is : ",array.ndim)

# Datatype of the array
print("Datatype of our Array is : ",array.dtype)

# computing log10 for the given array
print(np.lib.scimath.log10(array))
