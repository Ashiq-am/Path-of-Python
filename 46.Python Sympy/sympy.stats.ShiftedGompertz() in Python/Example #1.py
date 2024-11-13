# Import sympy and ShiftedGompertz
from sympy.stats import ShiftedGompertz, density
from sympy import Symbol, pprint

z = Symbol("z")
b = Symbol("b", positive = True)
eta = Symbol("eta", positive = True)

# Using sympy.stats.ShiftedGompertz() method
X = ShiftedGompertz("x", b, eta)
gfg = density(X)(z)

pprint(gfg)
