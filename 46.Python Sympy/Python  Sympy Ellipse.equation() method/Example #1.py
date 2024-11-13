# import sympy, Point and Ellipse
from sympy import Point, Ellipse
from sympy.abc import x, y

# using Ellipse()
e1 = Ellipse(Point(1, 0), 3, 2)

# using equation()
eq1 = e1.equation(x, y)

print(eq1)
