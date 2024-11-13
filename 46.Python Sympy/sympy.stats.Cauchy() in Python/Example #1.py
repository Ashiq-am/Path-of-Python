# Import sympy and cauchy
from sympy.stats import Cauchy, density
from sympy import Symbol

x0 = Symbol("x0")
gamma = Symbol("gamma", positive = True)
z = Symbol("z")

# Using sympy.stats.Cauchy() method
X = Cauchy("x", x0, gamma)
gfg = density(X)(z)

print(gfg)
