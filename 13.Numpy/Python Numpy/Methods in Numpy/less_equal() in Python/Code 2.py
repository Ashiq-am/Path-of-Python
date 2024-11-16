# Python Program illustrating
# numpy.less_equal() method

import numpy as geek

# Here we will compare Complex values with the
a = geek.array([100j, 7])
b = geek.array([1, 2])

print("Comparing complex with int : ", a <= b)

d = geek.less_equal(a, b)
print("\n Comparing complex with int .less_equal() : ", d)
