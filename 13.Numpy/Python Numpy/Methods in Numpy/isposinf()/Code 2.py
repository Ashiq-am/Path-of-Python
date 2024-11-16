# Python Program illustrating
# numpy.isposinf() method

import numpy as geek

# Returns True/False value for each element
b = geek.arange(18).reshape(3, 6)

print("\n", b)
print("\nIs Positive Infifnity : \n", geek.isposinf(b))

# geek.inf means Infinity
# geek.NINF means negative infinity
b = [[geek.inf],
     [geek.NINF]]
print("\nIs Positive Infifnity : \n", geek.isposinf(b))
