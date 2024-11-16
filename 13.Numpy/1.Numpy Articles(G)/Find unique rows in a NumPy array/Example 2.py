# import library
import numpy as np

# create 2d numpy array
array = np.array([[1, 2, 3, 4],
				[3, 2, 4, 1],
				[6, 8, 1, 2]])

print("Original array: \n", array)

# Get unique rows from
# complete 2D-array by
# passing axis = 0 in
# unique function along
# with 2D-array
uniqueRows = np.unique(array, axis = 0)

# print the output result
print('Unique Rows :', uniqueRows, sep = '\n')
