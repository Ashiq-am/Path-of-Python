# import trigintegrate
from sympy import Symbol, sin, cos, tan, sec, csc, cot
from sympy.integrals.trigonometry import trigintegrate
from sympy.abc import x

# Using trigintegrate() method
gfg = trigintegrate(tan(x)/cos(x), x)

print(gfg)
