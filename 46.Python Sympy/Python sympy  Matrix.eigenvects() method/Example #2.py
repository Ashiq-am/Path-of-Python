# import sympy
from sympy import *


M = Matrix([[1, -3, 3], [3, -5, 3], [6, -6, 4]])
print("Matrix : {} ".format(M))

# Use sympy.eigenvects() method
M_eigenvects = M.eigenvects()

print("Eigenvects of a matrix : {}".format(M_eigenvects))
