# import package
import numpy as np

# Creating arrays of coefficients
array = np.array([2, 3, 4])
array2 = np.array([5, 6, 7])
print(array)
print(array2)

# shape of the array is
print("Shape of the array1 is : ", array.shape)
print("Shape of the array2 is : ", array2.shape)

# dimension of the array
print("The dimension of the array1 is : ", array.ndim)
print("The dimension of the array2 is : ", array2.ndim)

# Datatype of the array
print("Datatype of our Array is : ", array.dtype)
print("Datatype of our Array2 is : ", array2.dtype)

# new array
print("Multiplication of two hermite series : ",
	np.polynomial.hermite.hermmul(array, array2))
