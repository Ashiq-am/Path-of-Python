# Python Program illustarting
# apply_over_axis() in NumPy

import numpy as geek

# Using a 3D array
geek_array = geek.arange(16).reshape(2, 2, 4)
print("geek array :\n", geek_array)

# Applying pre-defined sum function over the axis of 3D array
print("\nfunc sum : \n ", geek.apply_over_axes(geek.sum, geek_array, [1, 1, 0]))

# Applying pre-defined min function over the axis of 3D array
print("\nfunc min : \n ", geek.apply_over_axes(geek.min, geek_array, [1, 1, 0]))
