# Python program explaining
# numpy.nanstd() function

# importing numpy as geek
import numpy as geek

arr = geek.array([[1, 2], [geek.nan, 4]])

gfg = geek.nanstd(arr, axis=0)

print(gfg)
