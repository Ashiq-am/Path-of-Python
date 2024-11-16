# Python Program illustrating
# working of diag_indices()

import numpy as geek

# Manipulating a 2D array
d = geek.diag_indices(3, 2)

array = geek.arange(12).reshape(4, 3)

array[d] = 111
print("Manipulated array : \n", array)
