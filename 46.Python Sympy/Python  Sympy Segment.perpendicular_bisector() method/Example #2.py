# import sympy and Point, Segment
from sympy import Point, Segment

p1, p2, p3 = Point(0, 0), Point(6, 6), Point(5, 1)
s1 = Segment(p1, p2)

# using perpendicular_bisector() method
perpendicularBisector = s1.perpendicular_bisector(p3)

print(perpendicularBisector)
