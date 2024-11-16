# Python Program illustrating
# dot product of two vectors

# Importing numpy module
import numpy as np

# Taking two 2D array
# For 2-D arrays it is the matrix product
a = [[2, 1], [0, 3]]
b = [[1, 1], [3, 2]]

# Calculating dot product using dot()
# Note that here I have taken dot(b, a)
# Instead of dot(a, b) and we are going to
# get a different ouput for the same vector value
print(np.dot(b, a))
