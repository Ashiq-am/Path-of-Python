# Python Program illustrating
# numpy.less() method

import numpy as geek

# Here we will compare Float with int values
a = geek.array([1.1, 1])
b = geek.array([1, 2])

# indicating 1.1 is greater than 1
print("Comparing float with int : ", a < b)

# indicating 1.1 is greater than 1
d = geek.less(a, b)
print("\n Comparing float with int using .less() : ", d)
