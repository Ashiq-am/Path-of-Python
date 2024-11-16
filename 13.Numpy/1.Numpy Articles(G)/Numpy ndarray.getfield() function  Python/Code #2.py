# Python program explaining
# numpy.ndarray.getfield() function

# importing numpy as geek
import numpy as geek

x = geek.diag([2. + 2.j] * 2)

gfg = x.getfield(geek.float64, offset=8)

print(gfg)
