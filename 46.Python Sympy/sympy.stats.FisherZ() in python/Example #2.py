# Import sympy and FisherZ
from sympy.stats import FisherZ, density
from sympy import Symbol

d1 = 2
d2 = 3
z = 0.5

# Using sympy.stats.FisherZ() method
X = FisherZ("x", d1, d2)
gfg = density(X)(z)

print(gfg)
