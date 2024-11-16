# Python code to demonstrate
# deletion of columns from numpy array

import numpy as np

# initialising numpy array
ini_array = np.array([[1, 0, 0, 1, 0],
                      [0, 1, 2, 1, 1]])

# deleting second column from array
result = np.delete(ini_array, 1, 1)

# print result
print("Resultant Array :" + str(result))
