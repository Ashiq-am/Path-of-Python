# Import sympy and WignerSemicircle
from sympy.stats import WignerSemicircle, density
from sympy import Symbol, pprint

z = 0.87
r = 2

# Using sympy.stats.WignerSemicircle() method
X = WignerSemicircle("x", r)
gfg = density(X)(z)

pprint(gfg)
