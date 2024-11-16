# Python program explaining
# numpy.ma.filled() function

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

arr = geek.ma.array(geek.arange(4).reshape(2, 2),
                    mask=[[1, 0], [0, 1]])

gfg = arr.filled()

print(gfg)
