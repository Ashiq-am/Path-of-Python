# Python Program illustrating
# numpy.isposinf() method

import numpy as geek

print("Positive : ", geek.isposinf(1), "\n")

print("Positive : ", geek.isposinf(0), "\n")

# not a number
print("Positive : ", geek.isposinf(geek.nan), "\n")

# infinity
print("Positive : ", geek.isposinf(geek.inf), "\n")

print("Positive : ", geek.isposinf(geek.NINF), "\n")

x = geek.array([-geek.inf, 0., geek.inf])
y = geek.array([2, 2, 2])
print("Checking for positivity : ", geek.isposinf(x, y))
