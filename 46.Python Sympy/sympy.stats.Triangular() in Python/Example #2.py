# Import sympy and Triangular
from sympy.stats import Triangular, density
from sympy import Symbol, pprint

z = 5
a = 1.2
b = 1.3
c = 1.27

# Using sympy.stats.Triangular() method
X = Triangular("x", a, b, c)
gfg = density(X)(z)

pprint(gfg)
