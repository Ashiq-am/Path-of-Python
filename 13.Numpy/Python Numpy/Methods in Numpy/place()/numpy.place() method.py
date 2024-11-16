# Python Program illustrating
# numpy.place() method

import numpy as geek

array = geek.arange(12).reshape(3, 4)
print("Original array : \n", array)

# Putting new elements
a = geek.place(array, array > 5, [15, 25, 35])
print("\nPutting up elements to array: \n", array)


array1 = geek.arange(6).reshape(2, 3)
print("\n\nOriginal array1 : \n", array)

# Putting new elements
a = geek.place(array1, array1>2, [44, 55])
print("\nPutting new elements to array1 : \n", array1)
