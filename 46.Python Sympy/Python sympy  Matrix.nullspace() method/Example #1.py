# import sympy
from sympy import *

M = Matrix([[1, 0, 1, 3], [2, 3, 4, 7], [-1, -3, -3, -4]])
print("Matrix : {} ".format(M))

# Use sympy.nullspace() method
M_nullspace = M.nullspace()

print("Nullspace of a matrix : {}".format(M_nullspace))
