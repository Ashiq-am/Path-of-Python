# Python Program illustrating
# numpy.not_equal() method

import numpy as geek

# Here we will compare Complex values with int
a = geek.array([0 + 1j, 2])
b = geek.array([1, 2])

d = geek.not_equal(a, b)
print("Comparing complex with int using .not_equal() : ", d)
