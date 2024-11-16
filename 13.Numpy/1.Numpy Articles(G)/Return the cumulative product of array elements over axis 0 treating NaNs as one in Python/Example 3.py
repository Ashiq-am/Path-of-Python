# import packages
import numpy as np

# Creating an array with integers and nans
array = np.array([[10,np.nan],[np.nan,20]])
print(array)

# shape of the array is
print("Shape of the array is : ",array.shape)

# dimension of the array
print("The dimension of the array is : ",array.ndim)

# Datatype of the array
print("Datatype of our Array is : ",array.dtype)

# cumulative product of array elements along
# axis =1(along columns)
print(np.nancumprod(array,axis=1))
