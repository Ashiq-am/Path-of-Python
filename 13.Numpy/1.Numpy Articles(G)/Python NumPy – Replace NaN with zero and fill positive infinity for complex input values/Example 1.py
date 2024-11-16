import numpy as np

# array of imaginary numbers
array = np.array([complex(np.nan, np.inf)])
print(array)

# shape of the array is
print("Shape of the array is : ",array.shape)

# dimension of the array
print("The dimension of the array is : ",array.ndim)

# Datatype of the array
print("Datatype of our Array is : ",array.dtype)

# np.nan is replaced with 0.0 and np.inf
# is replaced with 999999
print("After replacement the array is : ",np.nan_to_num(array, posinf = 999999))
