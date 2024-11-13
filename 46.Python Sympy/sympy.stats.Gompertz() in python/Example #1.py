# Import sympy and Gompertz
from sympy.stats import Gompertz, density
from sympy import Symbol

b = Symbol("b", integer = True, positive = True)
eta = Symbol("eta", integer = True, positive = True)
z = Symbol("z")

# Using sympy.stats.Gompertz() method
X = Gompertz("x", b, eta)
gfg = density(X)(z)

print(gfg)
