# Python program for indexing using
# basic slicing with ellipsis
import numpy as np

# A 3 dimensional array.
b = np.array([[[1, 2, 3],[4, 5, 6]],
              [[7, 8, 9],[10, 11, 12]]])

print(b[...,1]) #Equivalent to b[: ,: ,1 ]
