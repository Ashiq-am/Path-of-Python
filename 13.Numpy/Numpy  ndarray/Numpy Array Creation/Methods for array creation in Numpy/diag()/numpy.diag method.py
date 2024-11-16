# Python Programming illustrating
# numpy.diag method

import numpy as geek

# matrix creation by array input
a = geek.matrix([[1, 21, 30],
				[63 ,434, 3],
				[54, 54, 56]])

print("Main Diagnol elements : \n", geek.diag(a), "\n")

print("Diagnol above main diagnol : \n", geek.diag(a, 1), "\n")

print("Diagnol below main diagnol : \n", geek.diag(a, -1))
