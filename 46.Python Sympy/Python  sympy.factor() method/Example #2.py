# import sympy
import sympy
from sympy import expand, symbols, factor

x, y, z = symbols('x y z')
gfg_exp = x + y + z
exp = sympy.expand(gfg_exp**2)

# Use sympy.factor() method
fact = factor(exp)

print(fact)
