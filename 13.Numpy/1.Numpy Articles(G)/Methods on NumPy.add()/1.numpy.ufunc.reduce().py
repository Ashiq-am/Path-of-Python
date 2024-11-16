# Reducing an array using np.add.reduce()

import numpy as np


# Array formation
a = np.arange(10)

# Reduction occurs column-wise with
# 'int' datatype
b = np.add.reduce(a, dtype = int, axis = 0)
print("The array {0} gets reduced to {1}".format(a, b))
