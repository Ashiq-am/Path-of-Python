# import sympy
from sympy import *


M = Matrix([[3, -2, 4, -2],
            [5, 3, -3, -2],
            [5, -2, 2, -2],
            [5, -2, -3, 3]])

print("Matrix : {} ".format(M))

# Use sympy.eigenvects() method
M_eigenvects = M.eigenvects()

print("Eigenvects of a matrix : {}".format(M_eigenvects))
