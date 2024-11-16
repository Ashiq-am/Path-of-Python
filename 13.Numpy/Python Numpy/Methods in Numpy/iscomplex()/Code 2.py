# Python Program illustrating
# numpy.iscomplex() method

import numpy as geek

# Returns True/False value for each element
a = geek.arange(20).reshape(5, 4)
print("Is complex : \n", geek.iscomplex(a))

# Returns True/False value as ans
# because we have mentioned dtpe in the begining
b = geek.arange(20).reshape(5, 4).dtype = complex

print("\n", b)
print("\nIs complex : ", geek.iscomplex(b))

b = [[1j],
     [3]]
print("\nIs complex : \n", geek.iscomplex(b))
