# import Curve, parameter and interpolate
from sympy.geometry.curve import Curve
from sympy.abc import t
from sympy import interpolate

# using interpolate() and Curve()
C1 = Curve((t, interpolate([1, 4, 9, 16], t)), (t, 0, 1))
print(C1)

# using translate()
C2 = C1.translate(2, 3)
print(C2)
