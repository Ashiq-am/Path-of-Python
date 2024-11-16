import numpy as npy

# creating a 2-d array
arr1 = npy.array([[1, 3, 5, 7], [2, 4, 6, 8]])

# creating a 3-d array
arr2 = npy.array([[1, 3, 5, 7], [2, 4, 6, 8],
				[3, 6, 9, 12]])

# printing the shape of arrays
# first element of tuple gives
# dimension of arrays second
# element of tuple gives number
# of element of each dimension
print(arr1.shape)
print(arr2.shape)
