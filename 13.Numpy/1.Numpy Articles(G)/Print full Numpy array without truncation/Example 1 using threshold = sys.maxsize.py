# Importing Numpy and sys modules
import numpy as np
import sys

# Creating a 1-D array with 100 values
arr = np.arange(101)

# Printing all values of array without truncation
np.set_printoptions(threshold=sys.maxsize)
print(arr)
