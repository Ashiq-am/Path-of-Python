# import package
import numpy as np

# Creating an array of complex numbers
array = np.array([10.0, 20+1.0j, 30+40j])
print(array)

# shape of the array is
print("Shape of the array is : ", array.shape)

# dimension of the array
print("The dimension of the array is : ", array.ndim)

# Datatype of the array
print("Datatype of our Array is : ", array.dtype)

# angle of the complex argument in radians
print("Angle in radians : ",
	np.angle(array))
