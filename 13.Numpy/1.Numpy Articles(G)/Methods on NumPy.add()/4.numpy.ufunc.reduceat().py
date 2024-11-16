# Reduceat method example

import numpy as np


a = np.arange(9)
z = np.add.reduceat(a, [1, 4, 2, 8])

print("Reduceat of matrix {} is {}".format(a,z))
