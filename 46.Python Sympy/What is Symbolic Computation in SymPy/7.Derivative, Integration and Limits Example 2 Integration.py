from sympy import *

x = Symbol('x')
e = Symbol('e')

expression = integrate(e**x, x)
expression
