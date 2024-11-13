# import packages
from sympy.abc import x
from sympy.logic.boolalg import Not

# nor formula
print(Not(x))

# ~True == True
print(Not(True))

# ~False == False
print(Not(False))
