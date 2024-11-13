# Import sympy and ContinuousRV
from sympy.abc import pi
from sympy.stats import ContinuousRV, P, E, density
from sympy import Symbol, pprint, sqrt

z = Symbol("z")
pdf = sqrt(2)*z / pi

# Using sympy.stats.ContinuousRV() method
X = ContinuousRV(z, pdf)
gfg = density(X)

pprint(gfg)
