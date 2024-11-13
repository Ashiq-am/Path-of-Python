# import sympy import Point, Polygon
from sympy import Point, Polygon

# creating points using Point()
p1, p2, p3 = map(Point, [(0, 0), (4, 0), (4, 4)])

# creating polygon using Polygon()
poly = Polygon(p1, p2, p3)

# using encloses_point()
isEnclosed = poly.encloses_point(Point(2, 2))

print(isEnclosed)
