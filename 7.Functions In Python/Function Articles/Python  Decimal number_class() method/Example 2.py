# Python Program explaining
# number_class() method

# loading decimal library
from decimal import *


# Initializing a decimal value
a = Decimal('-3.14')

b = Decimal('321e + 5')

# printing Decimal values
print ("Decimal value a : ", a)
print ("Decimal value b : ", b)


# Using Decimal.number_class() method
print ("\n\nDecimal a with number_class() method : ", a.number_class())

print ("Decimal b with number_class() method : ", b.number_class())
