# Python Program illustrating
# numpy.isnan() method

import numpy as geek

print("Is NaN : ", geek.isnan(1), "\n")

print("Is NaN : ", geek.isnan(0), "\n")

# not a number
print("Is NaN : ", geek.isnan(geek.nan), "\n")

# infinity
print("Is NaN : ", geek.isnan(geek.inf), "\n")

print("Is NaN : ", geek.isnan(geek.NINF), "\n")

x = geek.array([-geek.inf, 0., geek.inf])
y = geek.array([2, 2, 2])
print("Checking for NaN : ", geek.isnan(x, y))

