# import sympy
from sympy import *

x, y = symbols('x y')
exp = cos(3 * x) - sin(3 * y)
print("Before Trigonometric Expansion : {}".format(exp))

# Use sympy.expand_trig() method
res_exp = expand_trig(exp)

print("After Trigonometric Expansion : {}".format(res_exp))
