# importing packages
from sympy import RegularPolygon, Point

fig = RegularPolygon(Point(0, 0), 1, 3)

# area of the regular polygon
print(fig.area)
