# importing packages
from sympy.geometry import Ellipse, Point
from sympy.abc import x, y

# ellipse
ellipse = Ellipse(Point(0, 0), 5, 8)

# area of ellipse
print('area of the ellipse is : '+str(ellipse.area))

# equation of ellipse
print('equation of the ellipse is : ')
print(ellipse.equation(x, y))

# circumference of ellipse
print('circumference of the ellipse is : \
'+str(ellipse.circumference))
