# importing packages
import numpy as np

# creating arrays using np.array() method
# vector of letters
arr1 = np.array([5, 6, 7, 8], dtype=object)
# # integer array
arr2 = np.array([1, 2, 3, 4])
#
# # Display the arrays
print("Array of letters is :", arr1)
print("Array of numbers is :", arr2)
#
# # Checking the dimentions
print("Array one dimension :", arr1.ndim)
print("Array two dimension", arr2.ndim)
#
# # Checking the shape of the arrays
print("Shape of array 1 is : ", arr1.shape)
print("Shape of array 2 is : ", arr2.shape)

# # outer product of the vectors
print("Outer product : \n", np.outer(arr1, arr2))
