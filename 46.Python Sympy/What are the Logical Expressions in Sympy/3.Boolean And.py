# import packages
from sympy.abc import x, y
from sympy.logic.boolalg import And

res = x & y
print(res)

# 1&y ==y
print(And(x, y).subs(x, 1))

# 0&y ==0 or False
print(And(x, y).subs(x, 0))

# True&False == False
print(And(True, False))

# True & True == True
print(And(True, True))

# False & False == False
print(And(False, False))

# False & True == False
print(And(False, True))
