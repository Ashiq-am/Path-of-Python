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
