# import sympy and Relational
from sympy.core.relational import Relational
from sympy import *

x, y = symbols('x y')

# Using sympy.core.relational.Relational(var1, var2, "rel") method
gfg = Relational(x, y, ">=")

print(gfg)
