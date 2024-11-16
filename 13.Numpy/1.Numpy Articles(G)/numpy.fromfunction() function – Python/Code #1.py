# Python program explaining
# numpy.fromfunction() function

# importing numpy as geek
import numpy as geek

gfg = geek.fromfunction(lambda i, j: i * j, (4, 4), dtype=float)

print(gfg)
