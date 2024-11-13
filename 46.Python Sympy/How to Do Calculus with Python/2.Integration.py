# Indefinte integration of cos(x) w.r.t. dx
import sympy as sym
from sympy.abc import x

integral1 = sym.integrate(sym.cos(x), x)
print('indefinite integral of cos(x): ',integral1)

# definte integration of cos(x) w.r.t. dx between -1 to 1
integral2 = sym.integrate(sym.cos(x), (x, -1, 1))
print('definite integral of cos(x) between -1 to 1: ',integral2)

# definte integration of exp(-x) w.r.t. dx between 0 to ∞
integral3 = sym.integrate(sym.exp(-x), (x, 0, sym.oo))
print('definite integral of exp(-x) between 0 to ∞: ',integral3)
