# Import sympy and PowerFunction
from sympy.stats import PowerFunction, density
from sympy import Symbol, pprint

z = Symbol("z")
alpha = Symbol("alpha", positive = True)
a = Symbol("a", positive = True)
b = Symbol("b", positive = True)

# Using sympy.stats.PowerFunction() method
X = PowerFunction("x", alpha, a, b)
gfg = density(X)(z)

print(gfg)
