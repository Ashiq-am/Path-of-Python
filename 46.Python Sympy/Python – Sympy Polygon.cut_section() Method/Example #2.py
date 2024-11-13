# import sympy import Point, Polygon, Line
from sympy import Point, Polygon, Line

# creating points using Point()
p1, p2, p3, p4 = map(Point, [(0, 2), (0, 0), (1, 0), (1, 2)])

# creating polygon using Polygon()
poly = Polygon(p1, p2, p3, p4)

# using cut_section()
cutSection = poly.cut_section(Line((0, 1), slope = 1))

print(cutSection)
