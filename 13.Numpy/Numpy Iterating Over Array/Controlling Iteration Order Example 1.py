# Python program for
# iterating over array
# using particular order

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

print('Modified array in C-style order:')

# iterating an array in a given
# order
for x in geek.nditer(a, order='C'):
    print(x)