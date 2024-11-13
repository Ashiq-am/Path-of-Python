# assign series
import sympy as sym
from sympy.abc import x

series1 = sym.series(sym.cos(x), x)
print(series1)

# assign series
series2 = sym.series(1/sym.cos(x), x, 0, 4)
print(series2)
