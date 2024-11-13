# import sympy
from sympy import *

x, y, z = symbols('x y z')
exp = x ** 2 + 7 * y + z
print("Before Substitution : {}".format(exp))

# Use sympy.subs() method
res_exp = exp.subs([(x, 2), (y, 4), (z, 1)])

print("After Substitution : {}".format(res_exp))
