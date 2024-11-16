# Python Program illustrating
# numpy.isinf() method

import numpy as geek

print("Finite : ", geek.isinf(1), "\n")

print("Finite : ", geek.isinf(0), "\n")

# not a number
print("Finite : ", geek.isinf(geek.nan), "\n")

# infinity
print("Finite : ", geek.isinf(geek.inf), "\n")

print("Finite : ", geek.isinf(geek.NINF), "\n")

x = geek.array([-geek.inf, 0., geek.inf])
y = geek.array([2, 2, 2])
print("Checking for infinity : ", geek.isinf(x, y))
