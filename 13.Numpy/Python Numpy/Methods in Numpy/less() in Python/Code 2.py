# Python Program illustrating
# numpy.less() method

import numpy as geek

# Here we will compare Complex values with int
a = geek.array([1j, 2])
b = geek.array([1, 2])

# indicating 1j is lesser than 1
print("Comparing complex with int : ", a < b)

# indicating 1j is lesser than 1
d = geek.less(a, b)
print("\n Comparing complex with int .less() : ", d)
