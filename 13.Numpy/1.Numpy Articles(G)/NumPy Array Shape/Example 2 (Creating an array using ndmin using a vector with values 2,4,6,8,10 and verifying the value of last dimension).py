import numpy as npy

# creating an array of 6 dimension
# using ndim
arr = npy.array([2, 4, 6, 8, 10], ndmin=6)

# printing array
print(arr)

# verifying the value of last dimension
# as 5
print('shape of an array :', arr.shape)
