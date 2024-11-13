# import deltaintegrate
from sympy.abc import x, y, z
from sympy.integrals.deltafunctions import deltaintegrate
from sympy import sin, cos, DiracDelta, Heaviside

# Using deltaintegrate() method
gfg = deltaintegrate(sin(y)*DiracDelta(x - z)*DiracDelta(y - z), y)

print(gfg)
