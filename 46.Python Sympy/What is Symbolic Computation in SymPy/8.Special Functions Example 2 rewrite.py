from sympy import *

x = Symbol('x')
sec(x).rewrite(sin(x))
