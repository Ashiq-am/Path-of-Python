# import sympy
import sympy
from sympy import expand, symbols

x, y, z = symbols('x y z')
gfg_exp = x + y + z

# Use sympy.expand() method
exp = sympy.expand(gfg_exp**2)

print(exp)
