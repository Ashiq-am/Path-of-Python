# import singularityintegrate
from sympy.integrals.singularityfunctions import singularityintegrate
from sympy import SingularityFunction, symbols, Function

x, a, n, y = symbols('x a n y')
f = Function('f')

# Using singularityintegrate() method
gfg = singularityintegrate(SingularityFunction(x**3, 4, -2), x)

print(gfg)
