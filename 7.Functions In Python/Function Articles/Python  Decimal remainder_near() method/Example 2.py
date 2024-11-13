# Python Program explaining
# remainder_near() method

# loading decimal library
from decimal import *


# Initializing a decimal value
a = Decimal('-3.14')

b = Decimal('321e + 5')


# printing Decimal values
print ("Decimal value a : ", a)
print ("Decimal value b : ", b)


# Using Decimal.remainder_near() method
print ("\n\nDecimal a with remainder_near() method : ", a.remainder_near(b))

print ("Decimal b with remainder_near() method : ", b.remainder_near(b))
