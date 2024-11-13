# import sympy and geometry module
from sympy import *
from sympy.geometry import *

x = Point(0, 0)

# making line with given points
l = Line(Point(5, -5), Point(5, 5))

# making circle with Circle() of
# radius 5 and using is_tangent()
isTangent = Circle(x, 5).is_tangent(l)

print(isTangent)
