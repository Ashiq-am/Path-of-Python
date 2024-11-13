# import Point, Polygon
from sympy import Point, Polygon

# creating points using Point()
p1, p2, p3, p4 = map(Point, [(0, 0), (1, 0), (5, 1), (0, 1)])

# creating polygon using Polygon()
isConvex = Polygon(p1, p2, p3, p4)

# using is_convex()
print(isConvex.is_convex())
