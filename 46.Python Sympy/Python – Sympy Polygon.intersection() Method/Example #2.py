# import Point, Polygon
from sympy import Point, Polygon, Line

# creating points using Point()
p1, p2, p3, p4 = map(Point, [(0, 0), (1, 0), (5, 1), (0, 1)])

# creating polygon using Polygon()
poly1 = Polygon(p1, p2, p3, p4)

# using intersection()
isIntersection = poly1.intersection(Line(p1, Point(3, 2)))

print(isIntersection)
