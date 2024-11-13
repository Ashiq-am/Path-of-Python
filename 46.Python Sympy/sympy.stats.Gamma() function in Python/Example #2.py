# import sympy, Gamma, density, Symbol, pprint
from sympy.stats import Gamma, density
from sympy import Symbol, pprint

z = Symbol("z")

# using sympy.stats.Gamma() method
X = Gamma("x", 1 / 3, 45)
gamVar = density((X)(z))

pprint(gamVar)
