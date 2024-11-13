# Python Program explaining
# rotate() method

# loading decimal library
from decimal import *


# Initializing a decimal value
a = Decimal(1)

b = Decimal(2)

# printing Decimal values
print ("Decimal value a : ", a)
print ("Decimal value b : ", b)


# Using Decimal.rotate() method
print ("\n\nDecimal a with rotate() method : ", a.rotate(b))

print ("Decimal b with rotate() method : ", b.rotate(b))
