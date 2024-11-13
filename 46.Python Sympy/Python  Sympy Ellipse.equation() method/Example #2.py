# import sympy, Point and Ellipse
from sympy import Point, Ellipse
from sympy.abc import x, y

# using Ellipse()
e2 = Ellipse(Point(0, 0), 3, 2)

# using equation()
eq2 = e2.equation(x, y);

print(eq2)
