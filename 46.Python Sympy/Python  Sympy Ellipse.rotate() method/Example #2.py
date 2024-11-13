# import sympy and pi, Ellipse
from sympy import Ellipse, pi

# using Ellipse() method
e2 = Ellipse((1, 0), 2, 1)

# using rotate() with given point method
e2.rotate(pi / 2, (1, 2))

print(e2)
