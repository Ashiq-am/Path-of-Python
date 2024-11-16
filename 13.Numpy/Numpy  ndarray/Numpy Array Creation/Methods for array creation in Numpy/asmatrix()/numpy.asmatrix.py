# Python Programming illustrating
# numpy.asmatrix

import numpy as geek

# array-like input
b = geek.matrix([[5, 6, 7], [4, 6]])
print("Via array-like input : \n", b, "\n")

c = geek.asmatrix(b)
b[0, 1] = 10
print("c matrix : \n", c)
