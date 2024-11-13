# import sympy and geometry module
from sympy.geometry import Point, Ellipse

# using Ellipse()
e1 = Ellipse(Point(0, 0), 5, 1)

print(e1.hradius,e1.vradius)
