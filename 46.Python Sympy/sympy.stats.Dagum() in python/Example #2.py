# Import sympy and Dagum
from sympy.stats import Dagum, density
from sympy import Symbol

p = 3
a = 2
b = 5
z = 0.4

# Using sympy.stats.Dagum() method
X = Dagum("x", p, a, b)
gfg = density(X)(z)

print(gfg)
