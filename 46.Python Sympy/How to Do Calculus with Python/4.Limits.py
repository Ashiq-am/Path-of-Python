# Calculating limit of f(x) = x as x->∞
import sympy as sym
from sympy.abc import x

limit1 = sym.limit(x, x, sym.oo)
print(limit1)

# Calculating limit of f(x) = 1/x as x->∞
limit2 = sym.limit(1/x, x, sym.oo)
print(limit2)

# Calculating limit of f(x) = sin(x)/x as x->0
limit3 = sym.limit(sym.sin(x)/x, x, 0)
print(limit3)
