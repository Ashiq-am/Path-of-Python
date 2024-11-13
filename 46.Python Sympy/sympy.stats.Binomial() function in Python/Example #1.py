# Import sympy, Binomial, density
from sympy.stats import Binomial, density

# Using sympy.stats.Binomial() method
X = Binomial('X', 4, 1 / 3)
binDist = density(X).dict

print(binDist)
