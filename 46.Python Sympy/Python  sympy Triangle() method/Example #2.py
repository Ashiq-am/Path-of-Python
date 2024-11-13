# import sympy and geometry module
from sympy import *
from sympy.geometry import *

x = Point(1, 2)
y = Point(2, 0)
z = Point(1, 0)

# Using Triangle(x, y, z).area
giveArea = Triangle(x, y, z).area

print(giveArea)
