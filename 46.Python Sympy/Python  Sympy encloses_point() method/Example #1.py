# import sympy and geometry module
from sympy import *
from sympy.geometry import *

x = Point(0, 0)

# making ellipse with given point as center and radii
e1 = Ellipse(x, 3, 2)

# using encloses_point() method
isEnclosed = e1.encloses_point((0, 0))

print(isEnclosed)

