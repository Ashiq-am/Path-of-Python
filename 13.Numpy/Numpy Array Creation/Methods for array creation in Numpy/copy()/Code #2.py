# Python program explaining
# numpy.ndarray.copy() function

import numpy as geek


x = geek.array([[0, 1, ], [2, 3]])
print("x is:\n", x)

# copying x to y
y = x.copy()

# filling x with 1's
x.fill(1)
print("\n Now x is : \n", x)

print("\n y is: \n", y)
