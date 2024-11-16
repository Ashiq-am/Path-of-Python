# Python Program illustarting
# apply_along_axis() in NumPy

import numpy as geek

geek_array = geek.array([[8,1,7],
						[4,3,9],
						[5,2,6]])

# using pre-defined sorted function as 1D_func
print("Sorted as per axis 1 : \n", geek.apply_along_axis(sorted, 1, geek_array))

print("\n")

print("Sorted as per axis 0 : \n", geek.apply_along_axis(sorted, 0, geek_array))
