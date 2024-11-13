# Import sympy and WignerSemicircle
from sympy.stats import WignerSemicircle, density
from sympy import Symbol, pprint

z = Symbol("z")
r = Symbol("r", positive = True)

# Using sympy.stats.WignerSemicircle() method
X = WignerSemicircle("x", r)
gfg = density(X)(z)

pprint(gfg)
