# import sympy
from sympy import *

x = symbols('x')
exp = sin(2 * x) + cos(2 * x)
print("Before Trigonometric Expansion : {}".format(exp))

# Use sympy.expand_trig() method
res_exp = expand_trig(exp)

print("After Trigonometric Expansion : {}".format(res_exp))
