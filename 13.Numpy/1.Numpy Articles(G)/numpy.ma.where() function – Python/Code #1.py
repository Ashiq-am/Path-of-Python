# Python program explaining
# numpy.ma.where() function

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

x = geek.ma.array(geek.arange(4.).reshape(2, 2),
                  mask=[[0, 1], [1, 0]])

gfg = geek.ma.where(x > 5, x, -3.1416)

print(gfg)
