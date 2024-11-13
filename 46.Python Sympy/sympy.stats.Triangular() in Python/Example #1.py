# Import sympy and Triangular
from sympy.stats import Triangular, density
from sympy import Symbol, pprint

z = Symbol("z")
a = Symbol("a", positive = True)
b = Symbol("b", positive = True)
c = Symbol("c", positive = True)

# Using sympy.stats.Triangular() method
X = Triangular("x", a, b, c)
gfg = density(X)(z)

pprint(gfg)
