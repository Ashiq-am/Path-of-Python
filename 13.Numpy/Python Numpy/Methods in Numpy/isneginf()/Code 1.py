# Python Program illustrating
# numpy.isneginf() method

import numpy as geek

print("Negative : ", geek.isneginf(1), "\n")

print("Negative : ", geek.isneginf(0), "\n")

# not a number
print("Negative : ", geek.isneginf(geek.nan), "\n")

# infinity
print("Negative : ", geek.isneginf(geek.inf), "\n")

print("Negative : ", geek.isneginf(geek.NINF), "\n")

x = geek.array([-geek.inf, 0., geek.inf])
y = geek.array([2, 2, 2])
print("Checking for negativity : ", geek.isneginf(x, y))
