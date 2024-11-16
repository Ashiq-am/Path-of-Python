# Python Program illustrating
# numpy.isinf() method

import numpy as geek

# Returns True/False value for each element
b = geek.arange(8).reshape(2, 4)

print("\n", b)
print("\nIs Infifnity : \n", geek.isinf(b))

# geek.inf : Positive Infinity
# geek.NINF : negative Infinity
b = [[geek.inf],
     [geek.NINF]]
print("\nIs Infifnity : \n", geek.isinf(b))
