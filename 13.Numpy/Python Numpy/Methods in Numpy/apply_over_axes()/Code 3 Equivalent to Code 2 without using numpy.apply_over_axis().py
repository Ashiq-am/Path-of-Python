# Python Program illustarting
# equivalent to apply_over_axis()

import numpy as geek

# Using a 3D array
geek_array = geek.arange(16).reshape(2, 2, 4)
print("geek array :\n", geek_array)

# returning sum of all elements as per the axis
print("func : \n", geek.sum(geek_array, axis=(1, 0, 2), keepdims = True))
