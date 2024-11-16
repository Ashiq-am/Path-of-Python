# Python Program illustrating
# numpy.compress method

import numpy as geek

array = geek.arange(10).reshape(5, 2)
print("Original array : \n", array)

a = geek.compress([0, 1], array, axis=0)
print("\nSliced array : \n", a)

a = geek.compress([False, True], array, axis=0)
print("\nSliced array : \n", a)
