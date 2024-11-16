# importing required packages
import numpy as np

# declaring a numpy array
x = np.array([0, 1, 2, 3, 2, 5, 2, 7, 2, 9])

# calculating length of array
length = len(x)

# accessing every third element
# from the array
print("List after n=3rd element access")
print(x[0:length:3])
