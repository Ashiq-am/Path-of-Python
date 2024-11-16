# Python program for
# iterating array

import numpy as geek

# creating an array using arrange
# method
a = geek.arange(12)

# shape array with 3 rows and
# 4 columns
a = a.reshape(3, 4)

print('First array is:')
print(a)
print()

# Creating second array using
# array method
print('Second array is:')
b = geek.array([5, 6, 7, 8], dtype=int)
print(b)
print()

print('Modified array is:')
for x, y in geek.nditer([a, b]):
    print("%d:%d" % (x, y))
