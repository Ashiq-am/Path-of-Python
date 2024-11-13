# Import sympy and Exponential
from sympy.stats import Exponential, density
from sympy import Symbol

rate = 5
z = 0.5

# Using sympy.stats.Exponential() method
X = Exponential("x", rate)
gfg = density(X)(z)

print(gfg)
