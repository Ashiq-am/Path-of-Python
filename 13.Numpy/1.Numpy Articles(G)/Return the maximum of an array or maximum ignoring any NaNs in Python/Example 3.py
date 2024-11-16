import numpy as np

# Creating an array
array = np.array([np.nan, np.nan])
print(array)

# shape of the array is
print("Shape of the array is : ",array.shape)

# dimension of the array
print("The dimension of the array is : ",array.ndim)

# Datatype of the array
print("Datatype of our Array is : ",array.dtype)

# computing the maximum or array ignoring Nans
print(np.nanmax(array))
