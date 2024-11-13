# import sympy, Skellam, density
from sympy.stats import Skellam, density

# using sympy.stats.Skellam() method
X = Skellam("x", 1, 2)
skeDist = density(X)(3)

print(skeDist)
