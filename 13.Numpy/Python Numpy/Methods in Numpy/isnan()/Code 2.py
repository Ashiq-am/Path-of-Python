# Python Program illustrating
# numpy.isnan() method

import numpy as geek

# Returns True/False value for each element
b = geek.arange(20).reshape(5, 4)

print("\n", b)
print("\nIs NaN(Not a Number): \n", geek.isnan(b))

b = [[1j],
     [geek.nan]]
print("\nIs NaN(Not a Number) : \n", geek.isnan(b))
