# import packages
from sympy.abc import x, y
from sympy.logic.boolalg import Xor

xor_formula = x ^ y
print(xor_formula)
print(Xor(x, y))

# True ^ False == True
print(Xor(True, False))

# True ^ True == False
print(Xor(True, True))

# False ^ False == False
print(Xor(False, False))

# False ^ True == True
print(Xor(False, True))
