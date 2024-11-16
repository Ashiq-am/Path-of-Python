# Python Programming illustrating
# numpy.zeros_like method

import numpy as geek

array = geek.arange(10).reshape(5, 2)
print("Original array : \n", array)

array = geek.arange(4).reshape(2, 2)
c = geek.zeros_like(array, dtype = 'float')
print("\nMatrix : \n", c)

array = geek.arange(8)
c = geek.zeros_like(array, dtype = 'float', order ='C')
print("\nMatrix : \n", c)
