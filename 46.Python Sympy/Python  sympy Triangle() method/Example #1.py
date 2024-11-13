# import sympy and geometry module
from sympy import *
from sympy.geometry import *

x = Point(0, 0)
y = Point(1, 1)
z = Point(1, 0)

# Using Triangle(x, y, z).area
giveArea = Triangle(x, y, z).area

print(giveArea)
