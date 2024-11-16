# Python Program illustrating
# numpy.less() method

import numpy as geek

a = geek.less([8., 2.], [5., 3.])
print("Not equal : \n", a, "\n")

b = geek.less([2, 2], [[1, 3],[1, 4]])
print("Not equal : \n", b, "\n")

a = geek.array([4,2])
b = geek.array([6,2])

print("Is a lesser than b : ", a < b)
