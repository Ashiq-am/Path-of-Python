# Python Program explaining
# min_mag() method

# loading decimal library
from decimal import *


# Initializing a decimal value
a = Decimal(-1)

b = Decimal('0.142857')

# printing Decimal values
print ("Decimal value a : ", a)
print ("Decimal value b : ", b)


# Using Decimal.min_mag() method
print ("\n\nDecimal a with min_mag() method : ", a.min_mag(a))

print ("Decimal a with min_mag() method : ", a.min_mag(b))

print ("Decimal b with min_mag() method : ", b.min_mag(a))
