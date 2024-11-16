# Importing Numpy and sys modules
import numpy as np
import sys

# Creating a 1-D array with 50 values
arr = np.arange(51)

# Printing all values of array without truncation
np.set_printoptions(threshold=np.inf)
print(arr)
