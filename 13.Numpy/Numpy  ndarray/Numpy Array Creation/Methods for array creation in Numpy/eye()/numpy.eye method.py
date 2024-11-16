# Python Programming illustrating
# numpy.eye method

import numpy as geek

# 2x2 matrix with 1's on main diagnol
b = geek.eye(2, dtype = float)
print("Matrix b : \n", b)

# matrix with R=4 C=5 and 1 on diagnol
# below main diagnol
a = geek.eye(4, 5, k = -1)
print("\nMatrix a : \n", a)
