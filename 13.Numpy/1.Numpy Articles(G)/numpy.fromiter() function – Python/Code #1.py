# Python program explaining
# numpy.fromiter() function

# importing numpy as geek
import numpy as geek

iterable = (x * x * x for x in range(4))

gfg = geek.fromiter(iterable, int)

print(gfg)
