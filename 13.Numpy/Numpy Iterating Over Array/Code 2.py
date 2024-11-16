'''

'''


"""The order of iteration is chosen to match the memory layout of an array, without 
considering a particular ordering. This can be seen by iterating over the transpose of the 
above array."""

# Python program for
# iterating over transpose
# array

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

# Transpose of original array
b = a.T

print('Modified array is:')
for x in geek.nditer(b):
    print(x)