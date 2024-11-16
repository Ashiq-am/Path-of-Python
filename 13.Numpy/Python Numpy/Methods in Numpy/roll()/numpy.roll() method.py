# Python Program illustrating
# numpy.roll() method

import numpy as geek

array = geek.arange(12).reshape(3, 4)
print("Original array : \n", array)

# Rolling array; Shifting one place
print("\nRolling with 1 shift : \n", geek.roll(array, 1))

# Rolling array; Shifting five places
print("\nRolling with 5 shift : \n", geek.roll(array, 5))

# Rolling array; Shifting five places with 0th axis
print("\nRolling with 5 shift with 0 axis : \n", geek.roll(array, 2, axis = 0))
