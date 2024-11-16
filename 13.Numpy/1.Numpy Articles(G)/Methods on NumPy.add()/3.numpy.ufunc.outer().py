# To find the outer of two input arrays
import numpy as np


# Initialization of a 2x2 matrix
# as first input
a = np.arange(4).reshape(2,2)

# Initialization of an array as
# second input
b = np.arange(3)

# Outer of a & b
z = np.add.outer(b, a)

print("The outer of {0} & {1} is {2}".format(b,a,z))
