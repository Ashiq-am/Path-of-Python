# Import sympy and StudentT
from sympy.stats import StudentT, density
from sympy import Symbol, pprint

z = Symbol("z")
nu = Symbol("nu", positive = True)

# Using sympy.stats.StudentT() method
X = StudentT("x", nu)
gfg = density(X)(z)

pprint(gfg)
