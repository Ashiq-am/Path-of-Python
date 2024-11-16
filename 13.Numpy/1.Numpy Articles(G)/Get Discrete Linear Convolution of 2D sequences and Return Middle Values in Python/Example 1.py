# importing packages
import numpy as np

# creating arrays using np.array() method
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
#
# # Display the arrays
print("Array 1 is :", arr1)
print("Array 2 is :", arr2)
#
# # Checking the dimentions
print("Array one dimension :", arr1.ndim)
print("Array two dimension", arr2.ndim)
#
# # Checking the shape of the arrays
print("Shape of array 1 is : ", arr1.shape)
print("Shape of array 2 is : ", arr2.shape)

# returns the middle values of the convolution.
print("middle values of the convolution : \n",
	np.convolve(arr1, arr2, 'same'))
