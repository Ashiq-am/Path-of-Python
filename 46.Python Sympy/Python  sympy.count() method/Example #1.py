# importing sympy library
from sympy import *

# taking symbols
x, y, z = symbols('x y z')

# calling count() method on expression
geek = sqrt((x + 1)**2 + x).count(x)
print(geek)
