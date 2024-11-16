import numpy as np

# Creating an array
array = np.array([1+5j,3-6j])
print(array)

# shape of the array is
print("Shape of the array is : ",array.shape)

# dimension of the array
print("The dimension of the array is : ",array.ndim)

# Datatype of the array
print("Datatype of our Array is : ",array.dtype)

# returning real part
print(np.real_if_close(array, tol= 1000))
