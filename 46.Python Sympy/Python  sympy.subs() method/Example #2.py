# import sympy
from sympy import *

# symbol declaration
x, y = symbols('x y')

gfg_exp = cos(x) + 1

# use the method sympy.subs()
gfg_exp = gfg_exp.subs(x, 0)

print(gfg_exp)
