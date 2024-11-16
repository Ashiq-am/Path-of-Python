# Python program for
# iterating array values
# using f_index

import numpy as geek

# creating an array using arrange
# method
a = geek.arange(6)

# shape array with 2 rows and
# 3 columns
a = a.reshape(2, 3)

print('Original array is:')
print(a)
print()

# iterating array using f_index
# parameter
it = geek.nditer(a, flags=['f_index'])
while not it.finished:
    print("%d <%d>" % (it[0], it.index), end=" ")
    it.iternext()
