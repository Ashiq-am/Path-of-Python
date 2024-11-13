# Import sympy and Nakagami
from sympy.stats import Nakagami, density
from sympy import Symbol, pprint

z = 1.1
mu = 0.5
omega = 4

# Using sympy.stats.Nakagami() method
X = Nakagami("x", mu, omega)
gfg = density(X)(z)

pprint(gfg)
