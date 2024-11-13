# importing packages
from sympy.geometry import Point
from sympy.abc import a, b

# defining a point
p = Point(a, b)

# distance of the point from the origin
print(p.distance(Point(0, 0)))
