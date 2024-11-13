# import packages
from sympy.abc import x, y
from sympy.logic.boolalg import Nand

# not + nand == nand
nor_formula = ~(x & y)
print(nor_formula)
print(Nand(x, y))

# ~( True & False) == True
print(Nand(True, False))

# ~(True & True) == False
print(Nand(True, True))

# ~(False & False) == True
print(Nand(False, False))

# ~(False & True) == True
print(Nand(False, True))
