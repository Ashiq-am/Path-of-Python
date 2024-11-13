# import sympy import Point, Polygon, RegularPolygon
from sympy import Point, Polygon, RegularPolygon

# creating points using Point()
p1, p2 = map(Point, [(0, 0), (7, 5)])

# creating polygon using Polygon() and RegularPolygon()
poly = Polygon(*RegularPolygon(p1, 1, 3).vertices)

# using distance()
shortestDistance = poly.distance(p2)

print(shortestDistance)
