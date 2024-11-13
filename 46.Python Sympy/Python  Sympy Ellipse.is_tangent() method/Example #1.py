# import sympy and Point, Ellipse, Line
from sympy import Point, Ellipse, Line

p0, p1, p2 = Point(0, 0), Point(3, 0), Point(3, 3)

# using Line and Ellipse method
e1 = Ellipse(p0, 3, 2)
l1 = Line(p1, p2)

# using is_tangent method
e1.is_tangent(l1)
