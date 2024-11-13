# import sympy, Gamma, density, Symbol, pprint
from sympy.stats import Gamma, density
from sympy import Symbol, pprint

k = Symbol("k", positive = True)
theta = Symbol("theta", positive = True)
z = Symbol("z")

# using sympy.stats.Gamma() method
X = Gamma("x", k, theta)
gamVar = density((X)(z))

pprint(gamVar)
