# import sympy and geometry module
from sympy.geometry import Point, Circle

# using Circle()
c2 = Circle(Point(0, 0), Point(1, 1), Point(1, 0))

print(c2.hradius, c2.vradius, c2.radius)
