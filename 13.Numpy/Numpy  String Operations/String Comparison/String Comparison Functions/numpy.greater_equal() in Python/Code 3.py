# Python Program illustrating
# numpy.greater_equal() method

import numpy as geek

# Here we will compare Complex values with int
a = geek.array([1j, 2])
b = geek.array([1, 2])

print("Comparing complex with int : ", a < b)

d = geek.greater_equal(a, b)
print("\nComparing complex with int using .greater_equal() : ", d)
