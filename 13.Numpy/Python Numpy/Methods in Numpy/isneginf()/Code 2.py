# Python Program illustrating
# numpy.isneginf() method

import numpy as geek

# Returns True/False value for each element
b = geek.arange(18).reshape(3, 6)

print("\n", b)
print("\nIs Negative Infifnity : \n", geek.isneginf(b))

# geek.inf : Positive Infinity
# geek.NINF : negative Infinity
b = [[geek.inf],
     [geek.NINF]]
print("\nIs Negative Infifnity : \n", geek.isneginf(b))
