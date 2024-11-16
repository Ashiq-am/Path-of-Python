# Python Program illustrating
# numpy.isfinite() method

import numpy as geek

# Returns True/False value for each element
b = geek.arange(20).reshape(5, 4)

print("\n", b)
print("\nIs Finite : \n", geek.isfinite(b))

b = [[1j],
     [geek.inf]]
print("\nIs Finite : \n", geek.isfinite(b))
