# Python code to demonstrate
# deletion of columns from numpy array

import numpy as np

# initialising numpy array
ini_array = np.array([[1, 0, 0, 1, 0], [1, 2, 0, 0, 1]])
z = [False, True, False, False, False]

# deleting second column from array
result = ini_array.compress(np.logical_not(z), axis=1)

# print result
print("Resultant Array :" + str(result))
