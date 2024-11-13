# Import sympy and logarithmic
from sympy.stats import Logarithmic, density, E, variance
from sympy import Symbol, S

p = S.One / 5

# Using sympy.stats.Logarithmic() method
X = Logarithmic("x", p)
gfg = density(X)(3)

print(gfg)
