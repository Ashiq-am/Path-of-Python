# import sympy and geometry module
from sympy import *
from sympy.geometry import *

x = Point(0, 0)
y = Point(1, 1)
z = Point(2, 2)

# Using Ponit.is_collinear() method
isTrue = Point.is_collinear(x, y, z)

print(isTrue)
