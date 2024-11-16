# import library
import numpy as np

# Create a 2D numpy array
arr2D = np.array([[11, 11, 12, 11],
					[13, 11, 12, 11],
					[16, 11, 12, 11],
					[11, 11, 12, 11]])

print('Original Array :' , arr2D, sep = '\n')

# Get unique rows from
# complete 2D-array by
# passing axis = 0 in
# unique function along
# with 2D-array
uniqueRows = np.unique(arr2D, axis = 0)

# print the output result
print('Unique Rows:', uniqueRows, sep = '\n')
