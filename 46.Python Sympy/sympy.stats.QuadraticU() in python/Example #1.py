# Import sympy and QuadraticU
from sympy.stats import QuadraticU, density
from sympy import Symbol, pprint

z = Symbol("z")
a = Symbol("a", positive = True)
b = Symbol("b", positive = True)

# Using sympy.stats.QuadraticU() method
X = QuadraticU("x", a, b)
gfg = density(X)(z)

pprint(gfg)
