# import sympy
from sympy import *

# Use sympy.det() method
mat = Matrix([[1, 5, 1], [12, -1, 31], [4, 33, 2]])
d = mat.det()

print(d)
