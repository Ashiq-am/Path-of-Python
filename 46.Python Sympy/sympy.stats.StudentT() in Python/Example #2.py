# Import sympy and StudentT
from sympy.stats import StudentT, density
from sympy import Symbol, pprint

z = 0.46
nu = 2

# Using sympy.stats.StudentT() method
X = StudentT("x", nu)
gfg = density(X)(z)

pprint(gfg)
