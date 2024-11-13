from sympy.abc import x, y, z
from sympy.logic.boolalg import Equivalent, And, Or

print(Equivalent(x, y, z))

# true != false so it returns false
print(Equivalent(True, False))

# True == True so it returns true
print(Equivalent(True, True))

# False == False so it returns true
print(Equivalent(False, False))

# False !=True so it returns false
print(Equivalent(False, True))

# true ==true == true so it returns true
print(Equivalent(True, Or(True, False), And(True, True)))
