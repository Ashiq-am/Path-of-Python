import numpy as np

# Creating an array of imaginary numbers
array = np.array([1.+2.j , 2.+3.j , 4.+5.j])
print(array)

# dimension of the array
print("The dimension of the array is : ",array.ndim)

# Datatype of the array
print("Datatype of our Array is : ",array.dtype)

# shape of the array is
print("Shape of the array is : ",array.shape)

# numpy is real() method is used to return the
# real part of the imaginary numbers in the array
print("real part of the imaginary numbers in the array is :",np.real(array))
