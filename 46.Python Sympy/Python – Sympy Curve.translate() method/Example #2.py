# import Curve and parameter
from sympy.geometry.curve import Curve
from sympy.abc import x

# using Curve()
C1 = Curve((x, x), (x, 0, 1))
print(C1)

# using translate()
C2 = C1.translate(1, 2)
print(C2)
