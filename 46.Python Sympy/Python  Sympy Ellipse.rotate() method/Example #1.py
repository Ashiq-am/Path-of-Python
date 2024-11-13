# import sympy and pi, Ellipse
from sympy import Ellipse, pi

# using Ellipse() method
e1 = Ellipse((1, 0), 2, 1)

# using rotate() method
e1.rotate(pi / 2)

print(e1)
