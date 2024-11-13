# Import sympy and chi
from sympy.stats import Chi, density, E
from sympy import Symbol, simplify

k = 3
z = 2

# Using sympy.stats.Chi() method
X = Chi("x", k)
gfg = density(X)(z)

print(gfg)
