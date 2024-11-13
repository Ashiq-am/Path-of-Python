# import sympy and geometry module
from sympy.geometry import Point, Ellipse, Rational

# using Ellipse()
e2 = Ellipse(Point(3, 1), hradius=3, eccentricity=Rational(4, 5))

print(e2)
