import numpy as np


# Making of a 3x3 array
a = np.arange(9).reshape(3, 3)

# Vertical splitting of array 'a'
# using np.vsplit().
print("The array {} gets splitted vertically to form {} ".format(a, np.vsplit(a, 3)))

# Vertical splitting of array 'a'
# using 'split' with axis parameter = 0.
print("The array {} gets splitted vertically to form {} ".format(a, np.split(a, 3, 0)))
