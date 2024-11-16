# Python program explaining
# numpy.ma.allclose() function

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

a = geek.ma.array([1e10, 1e-8, 42.0], mask=[0, 0, 1])

b = geek.ma.array([1.00001e10, 1e-9, -42.0], mask=[0, 0, 1])

gfg = geek.ma.allclose(a, b)

print(gfg)
