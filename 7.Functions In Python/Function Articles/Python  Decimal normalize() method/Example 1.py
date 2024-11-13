# Python Program explaining
# normalize() method

# loading decimal library
from decimal import *


# Initializing a decimal value
a = Decimal(-1)

b = Decimal('0.142857')

# printing Decimal values
print ("Decimal value a : ", a)
print ("Decimal value b : ", b)


# Using Decimal.normalize() method
print ("\n\nDecimal a with normalize() method : ", a.normalize())

print ("Decimal b with normalize() method : ", b.normalize())
