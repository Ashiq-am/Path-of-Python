""""""


'''NumPy package contains an iterator object numpy.nditer. It is an efficient multidimensional 
iterator object using which it is possible to iterate over an array. Each element of an array is 
visited using Python’s standard Iterator interface.'''

# Python program for
# iterating over array

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

# iterating  an array
for x in geek.nditer(a):
    print(x)