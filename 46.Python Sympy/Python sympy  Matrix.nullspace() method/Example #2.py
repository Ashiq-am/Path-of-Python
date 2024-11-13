# import sympy
from sympy import *

M = Matrix([[14, 0, 11, 3], [22, 23, 4, 7], [-12, -34, -3, -4]])
print("Matrix : {} ".format(M))

# Use sympy.nullspace() method
M_nullspace = M.nullspace()

print("Nullspace of a matrix : {}".format(M_nullspace))
