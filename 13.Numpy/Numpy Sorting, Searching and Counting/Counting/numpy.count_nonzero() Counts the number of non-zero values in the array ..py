# Python Program illustrating
# working of count_nonzero()

import numpy as np

# Counting a number of
# non-zero values
from matplotlib.pyplot import axis

a = np.count_nonzero([[0, 1, 7, 0, 0], [3, 0, 0, 2, 19]])
b = np.count_nonzero(([[0, 1, 7, 0, 0], [3, 0, 0, 2, 19]],
                      axis))

print("Number of nonzero values is :", a)
print("Number of nonzero values is :", b)