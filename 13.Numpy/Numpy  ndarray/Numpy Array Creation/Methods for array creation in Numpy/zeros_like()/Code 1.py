# Python Programming illustrating
# numpy.zeros_like method

import numpy as geek

array = geek.arange(10).reshape(5, 2)
print("Original array : \n", array)


b = geek.zeros_like(array, float)
print("\nMatrix b : \n", b)

array = geek.arange(8)
c = geek.zeros_like(array)
print("\nMatrix c : \n", c)
