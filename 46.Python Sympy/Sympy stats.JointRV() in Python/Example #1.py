# Import sympy and JointRV
from sympy.abc import pi
from sympy.stats import JointRV, density
from sympy import Symbol, pprint

z = Symbol("z")
pdf = 2 * pi * z

# Using sympy.stats.JointRV() method
X = JointRV("x", pdf)
gfg = density(X)

pprint(gfg)
