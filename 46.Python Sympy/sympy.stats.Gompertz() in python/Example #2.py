# Import sympy and Gompertz
from sympy.stats import Gompertz, density
from sympy import Symbol

b = 2
eta = 4
z = 2

# Using sympy.stats.Gompertz() method
X = Gompertz("x", b, eta)
gfg = density(X)(z)

print(gfg)
