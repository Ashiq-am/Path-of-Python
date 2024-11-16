# import package
import numpy as np

# Creating an array of coefficients
array = np.array([11, 12, 13])
print(array)

# shape of the array is
print("Shape of the array is : ", array.shape)

# dimension of the array
print("The dimension of the array is : ", array.ndim)

# Datatype of the array
print("Datatype of our Array is : ", array.dtype)

# new array
print("new array: ",
	np.polynomial.hermite.hermmulx(array))
