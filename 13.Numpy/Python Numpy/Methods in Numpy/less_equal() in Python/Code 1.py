# Python Program illustrating
# numpy.less_equal() method

import numpy as geek

a = geek.less_equal([8., 2.], [5., 3.])
print("less_equal() : \n", a, "\n")

b = geek.less_equal([2, 2], [[1, 3],[1, 4]])
print("less_equal() : \n", b, "\n")

a = geek.array([4,3])
b = geek.array([6,2])

print("Is a less_equal than b : ", a <= b)
