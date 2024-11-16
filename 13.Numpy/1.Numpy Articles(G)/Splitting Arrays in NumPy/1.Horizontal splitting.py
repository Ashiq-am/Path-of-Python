# Horizontal array splitting using np.hsplit()
import numpy as np


# Making of a 3x3 array
a = np.arange(9).reshape(3, 3)

# Horizontal splitting of array
# 'a' using np.hsplit().
print("The array {} gets splitted horizontally to form {} ".format(a, np.hsplit(a, 3)))

# Horizontal splitting of array 'a'
# using 'split' with axis parameter = 1.
print("The array {} gets splitted horizontally to form {} ".format(a, np.split(a, 3, 1)))
