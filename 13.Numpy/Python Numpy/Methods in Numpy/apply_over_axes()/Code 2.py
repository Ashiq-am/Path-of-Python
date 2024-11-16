# Python Program illustarting
# apply_over_axis() in NumPy

import numpy as geek

# Using a 2D array
geek_array = geek.arange(16).reshape(4, 4)
print("geek array :\n", geek_array)

""" 
	->[[ 0 1 2 3] min : 0	 max : 3 sum = 0 + 1 + 2 + 3 
	-> [ 4 5 6 7] min : 4	 max : 7 sum = 4 + 5 + 6 + 7 
	-> [ 8 9 10 11] min : 8	 max : 11 sum = 8 + 9 + 10 + 11 
	-> [12 13 14 15]] min : 12 max : 15 sum = 12 + 13 + 14 + 15 

"""

# Applying pre-defined min function over the axis of 2D array
print("\nApplying func max : \n ", geek.apply_over_axes(geek.max, geek_array, [1, -1]))

# Applying pre-defined min function over the axis of 2D array
print("\nApplying func min : \n ", geek.apply_over_axes(geek.min, geek_array, [1, -1]))

# Applying pre-defined sum function over the axis of 2D array
print("\nApplying func sum : \n ", geek.apply_over_axes(geek.sum, geek_array, [1, -1]))
