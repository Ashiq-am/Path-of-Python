# import sympy and Point, Line, Segment
from sympy import Point, Line, Segment

p1, p2, p3, p4 = Point(0, 0), Point(1, 1), Point(0, 5), Point(2, 6)
l1 = Line(p1, p2)
s1 = Segment(p3, p4)


# using intersection() method
showIntersection = l1.intersection(s1)

print(showIntersection)
