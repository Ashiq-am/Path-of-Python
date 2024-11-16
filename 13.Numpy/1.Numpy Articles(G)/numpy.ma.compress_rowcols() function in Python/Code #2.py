# Python program explaining
# numpy.ma.compress_rowcols() function

# importing numpy as geek
import numpy as geek

arr = geek.ma.array(geek.arange(6).reshape(2, 3),
					mask=[[1, 0, 0], [0, 0, 0]])

gfg = geek.ma.compress_rowcols(arr, 1)

print(gfg)
