""""""


'''Ellipsis can also be used along with basic slicing. Ellipsis (…) is the number of : objects 
needed to make a selection tuple of the same length as the dimensions of the array.'''



# Python program for indexing using
# basic slicing with ellipsis
import numpy as np

# A 3 dimensional array.
b = np.array([[[1, 2, 3], [4, 5, 6]],
              [[7, 8, 9], [10, 11, 12]]])

print(b[..., 1])  # Equivalent to b[: ,: ,1 ]