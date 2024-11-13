# Import sympy and Exponential
from sympy.stats import Exponential, density
from sympy import Symbol

rate = Symbol("rate", integer = True, positive = True)
z = Symbol("z")

# Using sympy.stats.Exponential() method
X = Exponential("x", rate)
gfg = density(X)(z)

print(gfg)
