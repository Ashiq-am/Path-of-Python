# Python code to demonstrate
# deletion of columns from numpy array

import numpy as np

# initialising numpy array
ini_array = np.array([['manjeet', 'akshat'], ['nikhil', 'akash']])

# convert numpy arrays into tuples
result = tuple([tuple(row) for row in ini_array])

# print result
print("Result:" + str(result))
