import numpy as np

# Creating an array
array = np.arr([complex(-2, -1),complex(-5, -3)])
print(array)

# shape of the array is
print("Shape of the array is : ",arr.shape)

# dimension of the array
print("The dimension of the array is : ",arr.ndim)

# Datatype of the array
print("Datatype of our Array is : ",arr.dtype)

# computing the square root of complex inputs
print(np.emath.sqrt(arr))
