# import sympy, Point3D and Plane
from sympy import Point3D, Plane

o = (0, 0, 0)

# using Plane()
p1 = Plane(o, (1, 1, 1))
p2 = Plane(o, (2, 2, 2))

# using is_coplanar()
isCoplanar = p1.is_coplanar(p2)

print(isCoplanar)
