# import sympy and geometry module
from sympy import *
from sympy.geometry import *

x = Point(0, 0)
y = Point(1, 1)

# making line with given points
l = Line(x, y)

# making circle with Circle() of radius 5 and using is_tangent()
isTangent = Circle(x, 5).is_tangent(l)

print(isTangent)
