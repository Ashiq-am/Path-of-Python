# import packages
from sympy.abc import x, y
from sympy.logic.boolalg import Or

res = x | y
print(res)

# 1&y == 1 or True
print(Or(x, y).subs(x, 1))

# 0|y ==y
print(Or(x, y).subs(x, 0))

# True | False == True
print(Or(True, False))

# True | True == True
print(Or(True, True))

# False | False == False
print(Or(False, False))

# False | True == True
print(Or(False, True))
