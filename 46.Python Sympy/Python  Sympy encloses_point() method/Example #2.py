# import sympy and geometry module
from sympy import *
from sympy.geometry import *

x = Point(3, 1)

# making ellipse with given point as center, hradius and eccentricity
e2 = Ellipse(x, hradius = 3, eccentricity = Rational(4, 5))

# using encloses_point() method
isEnclosed = e2.encloses_point((4, 6))

print(isEnclosed)

