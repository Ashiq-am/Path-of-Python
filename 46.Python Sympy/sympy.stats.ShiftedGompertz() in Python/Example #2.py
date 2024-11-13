# Import sympy and ShiftedGompertz
from sympy.stats import ShiftedGompertz, density
from sympy import Symbol, pprint

z = 1.1
b = 2
eta = 3

# Using sympy.stats.ShiftedGompertz() method
X = ShiftedGompertz("x", b, eta)
gfg = density(X)(z)

pprint(gfg)
