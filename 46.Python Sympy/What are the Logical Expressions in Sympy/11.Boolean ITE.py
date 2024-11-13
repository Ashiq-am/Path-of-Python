from sympy.abc import x, y, z
from sympy.logic.boolalg import ITE, Nor, Nand, Xor, Or, And

# ITE == if then else
print(ITE(x, y, z))

# x is true so y is returned
print(ITE(True, Or(True, False), And(True, True)))

# x is false so z is returned
print(ITE(Nor(True, False), Xor(True, False), Nand(True, True)))
