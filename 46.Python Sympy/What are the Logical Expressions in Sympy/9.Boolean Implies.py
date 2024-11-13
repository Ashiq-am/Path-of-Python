from sympy.abc import x, y
from sympy.logic.boolalg import Implies

# !A v B == implies formula
# returns false when A is true and B is
# false, rest all cases returns True
print(Implies(x, y))

# false
print(Implies(True, False))

# true
print(Implies(True, True))

# true
print(Implies(False, False))

# true
print(Implies(False, True))
print(x << y)
print(x >> y)
