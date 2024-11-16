# Python Program illustrating
# numpy.isfinite() method

import numpy as geek

print("Finite : ", geek.isfinite(1), "\n")

print("Finite : ", geek.isfinite(0), "\n")

# not a number
print("Finite : ", geek.isfinite(geek.nan), "\n")

# infinity
print("Finite : ", geek.isfinite(geek.inf), "\n")

print("Finite : ", geek.isfinite(geek.NINF), "\n")
