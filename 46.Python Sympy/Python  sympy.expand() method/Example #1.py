# import sympy
import sympy
from sympy import expand, symbols

x, y = symbols('x y')
gfg_exp = x + y

# Use sympy.expand() method
exp = sympy.expand(gfg_exp**2)

print(exp)
