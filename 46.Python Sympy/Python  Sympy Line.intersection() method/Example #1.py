# import sympy and Point, Line
from sympy import Point, Line

p1, p2, p3 = Point(0, 0), Point(1, 1), Point(7, 7)
l1 = Line(p1, p2)

# using intersection() method
showIntersection = l1.intersection(p3)

print(showIntersection)
