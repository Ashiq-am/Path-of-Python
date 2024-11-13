# import sympy
from sympy import *

# Use sympy.det() method
mat = Matrix([[1, 0, 1], [2, -1, 3], [4, 3, 2]])
d = mat.det()

print(d)
