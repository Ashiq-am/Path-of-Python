# Python program explaining
# numpy.ndarray.setfield() function

# importing numpy as geek
import numpy as geek

arr = geek.eye(2)

arr.setfield(2, geek.int32)
gfg = arr.getfield(geek.int32)

print(gfg)
