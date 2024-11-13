# Import sympy and QuadraticU
from sympy.stats import QuadraticU, density
from sympy import Symbol, pprint

z = 1.5
a = 4
b = 6

# Using sympy.stats.QuadraticU() method
X = QuadraticU("x", a, b)
gfg = density(X)(z)

pprint(gfg)
