# Import sympy and Dagum
from sympy.stats import Dagum, density
from sympy import Symbol

p = Symbol("p", integer = True, positive = True)
a = Symbol("a", integer = True, positive = True)
b = Symbol("b", integer = True, positive = True)
z = Symbol("z")

# Using sympy.stats.Dagum() method
X = Dagum("x", p, a, b)
gfg = density(X)(z)

print(gfg)
