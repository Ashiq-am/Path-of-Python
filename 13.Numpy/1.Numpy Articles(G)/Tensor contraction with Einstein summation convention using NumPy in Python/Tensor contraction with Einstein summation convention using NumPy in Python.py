# import packages
import numpy as np

# np.arange() method is used to create
# two arrays
arr1 = np.arange(12).reshape(2,2,3)
arr2 = np.arange(12).reshape(2,2,3)

# Display the arrays
print("Array of letters is :",arr1)
print("Array of numbers is :",arr2)

# Checking the dimentions
print("Array one dimension :",arr1.ndim)
print("Array two dimension",arr2.ndim)

# Checking the shape of the arrays
print("Shape of array 1 is : ",arr1.shape)
print("Shape of array 2 is : ",arr2.shape)

# Tensor contraction with Einstein summation convention
print("Tensor contraction : ",np.einsum('ijk,jil->kl', arr1, arr2))
