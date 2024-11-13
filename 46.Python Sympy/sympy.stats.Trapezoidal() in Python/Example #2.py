# Import sympy and Trapezoidal
from sympy.stats import Trapezoidal, density
from sympy import Symbol, pprint

z = 0.43
a = 2
b = 4
c = 5
d = 8

# Using sympy.stats.Trapezoidal() method
X = Trapezoidal("x", a, b, c, d)
gfg = density(X)(z)

pprint(gfg)
