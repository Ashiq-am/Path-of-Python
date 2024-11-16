# Python Program illustrating
# numpy.empty_like method

import numpy as geek

a = geek.empty_like([2, 2], dtype = int)
print("\nMatrix a : \n", a)

c = a = ([1,2,3], [4,5,6])
print("\nMatrix c : \n", geek.empty_like(c))
