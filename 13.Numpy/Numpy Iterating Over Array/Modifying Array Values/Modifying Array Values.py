# Python program for
# modifying array values

import numpy as geek

# creating an array using arrange
# method
a = geek.arange(12)

# shape array with 3 rows and
# 4 columns
a = a.reshape(3, 4)
print('Original array is:')
print(a)
print()

# modifying array values
for x in geek.nditer(a, op_flags=['readwrite']):
    x[...] = 5 * x
print('Modified array is:')
print(a)