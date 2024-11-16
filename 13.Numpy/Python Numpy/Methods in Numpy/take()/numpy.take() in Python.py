# Python Program illustrating
# numpy.take method

import numpy as geek

#array = geek.arange(10).reshape(2, 5)
array = [[5, 6, 2, 7, 1],
		[4, 9, 2, 9, 3]]
print("Original array : \n", array)

# indices = [0, 4]
print("\nTaking Indices\n", geek.take(array, [0, 4]))

# indices = [0, 4] with axis = 1
print("\nTaking Indices\n", geek.take(array, [0, 4], axis = 1))
