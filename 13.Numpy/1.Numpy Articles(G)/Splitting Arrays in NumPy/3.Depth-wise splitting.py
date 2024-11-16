import numpy as np


# Making of a 3x3x3 array.
b = np.arange(27).reshape(3, 3, 3)

# Depth-wise splitting of array
# 'b' using np.dsplit().
print("The array {} gets splitted depth-wise to form {}".format(b, np.dsplit(b, 3)))
