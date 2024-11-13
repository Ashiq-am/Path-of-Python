# import sympy and Point, Line
from sympy import Point, Line

p1, p2 = Point(0, 0), Point(1, 1)
s = Line(p1, p2)

# using distance() method
shortestDistance = s.distance(Point(-1, 1))

print(shortestDistance)
