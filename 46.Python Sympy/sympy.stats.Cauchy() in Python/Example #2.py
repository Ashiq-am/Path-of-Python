# Import sympy and cauchy
from sympy.stats import Cauchy, density
from sympy import Symbol

x0 = 2
gamma = 3
z = 0.5

# Using sympy.stats.Cauchy() method
X = Cauchy("x", x0, gamma)
gfg = density(X)(z)

print(gfg)
