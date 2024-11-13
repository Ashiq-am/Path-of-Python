# import sympy, Point3D and Plane
from sympy import Point3D, Plane

o = (0, 0, 0)

# using Plane()
p3 = Plane(o, (1, 1, 1))
p4 = Plane(o, (3, 2, 1))

# using is_coplanar()
isCoplanar = p3.is_coplanar(p4)

print(isCoplanar)
