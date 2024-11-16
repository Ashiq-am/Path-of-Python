import numpy as np

# Creating an array
array = np.array([1,2,-3, -4])
print(array)

# shape of the array is
print("Shape of the array is : ",array.shape)

# dimension of the array
print("The dimension of the array is : ",array.ndim)

# Datatype of the array
print("Datatype of our Array is : ",array.dtype)

# computing inverse cosine
print(np.emath.arccos(array))
