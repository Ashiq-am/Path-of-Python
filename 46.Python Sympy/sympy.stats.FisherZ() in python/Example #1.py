# Import sympy and FisherZ
from sympy.stats import FisherZ, density
from sympy import Symbol

d1 = Symbol("d1", integer = True, positive = True)
d2 = Symbol("d2", integer = True, positive = True)
z = Symbol("z")

# Using sympy.stats.FisherZ() method
X = FisherZ("x", d1, d2)
gfg = density(X)(z)

print(gfg)
