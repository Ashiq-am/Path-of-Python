# Import sympy and logarithmic
from sympy.stats import Logarithmic, density, E, variance
from sympy import Symbol, S

p = 0.46

# Using sympy.stats.Logarithmic() method
X = Logarithmic("x", p)
gfg = density(X)(4)

print(gfg)
