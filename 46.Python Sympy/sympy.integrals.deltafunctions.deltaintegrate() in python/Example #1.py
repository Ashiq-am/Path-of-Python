# import deltaintegrate
from sympy.abc import x, y, z
from sympy.integrals.deltafunctions import deltaintegrate
from sympy import sin, cos, tan, DiracDelta, Heaviside

# Using deltaintegrate() method
gfg = deltaintegrate(tan(x)*sin(x)*cos(x)*DiracDelta(x**2 - 1), x)

print(gfg)
