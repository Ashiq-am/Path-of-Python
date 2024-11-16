# Python Program illustrating
# numpy.greater() method

import numpy as geek

a = geek.greater([8., 2.], [5., 3.])
print("Not equal : \n", a, "\n")

b = geek.greater([2, 2], [[1, 3],[1, 4]])
print("Not equal : \n", b, "\n")

a = geek.array([4,2])
b = geek.array([6,2])

print("Is a greater than b : ", a > b)
