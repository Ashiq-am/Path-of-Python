# Python Program illustrating
# numpy.fliplr() method

import numpy as geek

array = geek.arange(8).reshape((2,2,2))
print("Original array : \n", array)

# fliplr : means flip left-right
print("\nFlipped array left-right : \n", geek.fliplr(array))
