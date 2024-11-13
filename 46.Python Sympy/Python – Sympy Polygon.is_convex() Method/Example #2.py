# import Point, Polygon
from sympy import Point, Polygon

# creating points using Point()
p1, p2, p3, p4, p5 = map(Point, [(0, 0), (3, 2), (4, 5), (7, 1), (6, 3)])

# creating polygon using Polygon()
isConvex = Polygon(p1, p2, p3, p4, p5)

# using is_convex()
print(isConvex.is_convex())
