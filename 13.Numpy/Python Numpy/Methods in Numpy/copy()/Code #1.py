# Python program explaining
# numpy.ndarray.copy() function

import numpy as geek


x = geek.array([[0, 1, 2, 3], [4, 5, 6, 7]],
								order ='F')
print("x is: \n", x)

# copying x to y
y = x.copy()
print("y is :\n", y)
print("\nx is copied to y")
