# importing numpy module
import numpy as np

# list 1 represents an array
# with integer values
list1 = [1, 2, 3, 4, 5, 0]

# list 2 represents an array
# with integer values
list2 = [0, 1, 2, 3, 4, 0]

# logical operations between integer values
print('Operation between two lists:',
	np.logical_and(list1, list2))
