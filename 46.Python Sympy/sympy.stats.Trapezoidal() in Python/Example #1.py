# Import sympy and Trapezoidal
from sympy.stats import Trapezoidal, density
from sympy import Symbol, pprint

z = Symbol("z")
a = Symbol("a", positive = True)
b = Symbol("b", positive = True)
c = Symbol("c", positive = True)
d = Symbol("d", positive = True)

# Using sympy.stats.Trapezoidal() method
X = Trapezoidal("x", a, b, c, d)
gfg = density(X)(z)

pprint(gfg)
