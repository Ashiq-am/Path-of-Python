# import package
import numpy as np

# Creating an array represebting polynomial
array = np.array([11,22,33])
print(array)

# shape of the array is
print("Shape of the array1 is : ",array.shape)

# dimension of the array
print("The dimension of the array1 is : ",array.ndim)

# Datatype of the array
print("Datatype of our Array is : ",array.dtype)

# converting polynomial to chebyshev series
print("polynomial to chebyshev series : ",
	np.polynomial.chebyshev.poly2cheb(array))
