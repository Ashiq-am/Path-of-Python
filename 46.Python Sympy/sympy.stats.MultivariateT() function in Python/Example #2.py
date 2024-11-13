# import sympy, MultivariateT, density, Symbol
from sympy.stats import density, MultivariateT
from sympy import Symbol, pprint

x = Symbol("x")

# using sympy.stats.MultivariateT() method
X = MultivariateT("x", [1, 1, 1], [[1, 0, 1], [0, 1, 0], [0, 0, 1]], 1 / 2)
multiVar = density(X)(1, 2, 3)

pprint(multiVar)
