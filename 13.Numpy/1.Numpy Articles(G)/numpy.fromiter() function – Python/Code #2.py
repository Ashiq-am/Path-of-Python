# Python program explaining
# numpy.fromiter() function

# importing numpy as geek
import numpy as geek

iterable = (x * x for x in range(6))

gfg = geek.fromiter(iterable, float)

print(gfg)
