# import packages
from sympy.abc import x, y
from sympy.logic.boolalg import Nor

nor_formula = ~(x | y)
print(nor_formula)
print(Nor(x, y))

# ~( True | False) == False
print(Nor(True, False))

# ~(True | True) == False
print(Nor(True, True))

# ~(False | False) == True
print(Nor(False, False))

# ~(False | True) == False
print(Nor(False, True))
