# Import sympy and Kumaraswamy
from sympy.stats import Kumaraswamy, density
from sympy import Symbol, pprint

z = Symbol("z")
a = Symbol("a", positive = True)
b = Symbol("b", positive = True)

# Using sympy.stats.Kumaraswamy() method
X = Kumaraswamy("x", a, b)
gfg = density(X)(z)

pprint(gfg)
