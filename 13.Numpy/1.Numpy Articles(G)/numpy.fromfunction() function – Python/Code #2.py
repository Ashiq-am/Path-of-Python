# Python program explaining
# numpy.fromfunction() function

# importing numpy as geek
import numpy as geek

gfg = geek.fromfunction(lambda i, j: i == j, (3, 3), dtype=int)

print(gfg)
