# Python program for
# iterating array values
# using external loop

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

print('Modified array is:')
for x in geek.nditer(a, flags=['external_loop'], order='C'):
    print(x)