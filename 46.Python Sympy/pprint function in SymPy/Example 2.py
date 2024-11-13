# import everything from sympy module
from sympy import *

x, y, z, t = symbols('x y z t')
pprint(Integral(sqrt(x)*((x**3)/y), x), use_unicode=True)
