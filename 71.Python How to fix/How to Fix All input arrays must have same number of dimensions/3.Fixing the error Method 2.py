# Importing numpy library
import numpy as np

# Creating a numpy array with demension 2 * 2
np_array1 = np.array([[2, 3],[2,4]])

# Creating a numpy array with demension 2 * 3
np_array2 = np.array([[8, 9,10], [10,11,12]])

# Using the column_stack() function
np_array3 = np.column_stack((np_array1,np_array2))
print(np_array3)
