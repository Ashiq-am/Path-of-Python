# Python Program illustrating
# numpy.less_equal() method

import numpy as geek

# Here we will compare Float with int values
a = geek.array([1.1, 1])
b = geek.array([1, 2])

print("Comparing float with int : ", a <= b)

d = geek.less_equal(a, b)
print("\n Comparing float with int using .less_equal() : ", d)
