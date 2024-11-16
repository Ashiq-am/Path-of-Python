# import packages
import numpy as np

# Creating an array
array = np.array([[10,20],[30,40]])
print(array)

# shape of the array is
print("Shape of the array is : ",array.shape)

# dimension of the array
print("The dimension of the array is : ",array.ndim)

# Datatype of the array
print("Datatype of our Array is : ",array.dtype)

# computing sign and natural logarithm of the
# determinant of the array
sign, determinant= (np.linalg.slogdet(array))

print('sign of the array is : '+str(sign))

print('logarithm of the determinant of the array is : '+ str(determinant))
