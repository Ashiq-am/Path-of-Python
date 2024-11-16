# import package
import numpy as np

# Creating an array of imaginary numbers
array = np.array([complex(np.nan, -np.inf),1,2, np.inf])
print(array)

# shape of the array is
print("Shape of the array is : ",array.shape)

# dimension of the array
print("The dimension of the array is : ",array.ndim)

# Datatype of the array
print("Datatype of our Array is : ",array.dtype)

# np.nan is replaced with 100 and np.inf is
# replaced with 100000 negative infinity is replaced with 999999
print("After replacement the array is: ",
	np.nan_to_num(array,nan= 100, posinf = 100000, neginf=999999))
