# Import sympy and Nakagami
from sympy.stats import Nakagami, density
from sympy import Symbol, pprint

z = Symbol("z")
mu = Symbol("mu", positive = True)
omega = Symbol("omega", positive = True)

# Using sympy.stats.Nakagami() method
X = Nakagami("x", mu, omega)
gfg = density(X)(z)

pprint(gfg)
