# importing numpy module
import numpy as np

# list 1 represents an array with boolean values
list1 = [True, False, True, False]

# list 2 represents an array with boolean values
list2 = [True, True, False, True]

# logical operations between boolean values
print('Operation between two lists = ',np.logical_and(list1, list2))
