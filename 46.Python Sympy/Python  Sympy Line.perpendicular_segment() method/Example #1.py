# import sympy and Point, Line
from sympy import Point, Line

p1, p2, p3 = Point(0, 0), Point(1, 1), Point(0, 2)
l1 = Line(p1, p2)

# using perpendicular_segment() method
perpendicularSegment = l1.perpendicular_segment(p3)

print(perpendicularSegment)
