# import sympy, MultivariateEwens, density, Symbol
from sympy.stats.joint_rv_types import MultivariateEwens
from sympy.stats import density
from sympy import Symbol, pprint

a = Symbol('a', positive = True)
b = Symbol('b', positive = True)

# using sympy.stats.MultivariateEwens() method
E = MultivariateEwens('E', 2, 1)
mveDist = density(E)(a, b)

pprint(mveDist)
