# importing sympy library
from sympy import *

# taking symbols
x, y, z = symbols('x y z')

# calling find() method on expression
geek = (3 * x + log(3 * x) + sqrt((x + 1)**2 + x)).find(log)
print(geek)
