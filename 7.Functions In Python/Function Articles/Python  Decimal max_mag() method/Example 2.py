# Python Program explaining
# max_mag() method

# loading decimal library
from decimal import *


# Initializing a decimal value
a = Decimal('-3.14')

b = Decimal('321e + 5')

# printing Decimal values
print ("Decimal value a : ", a)
print ("Decimal value b : ", b)


# Using Decimal.max_mag() method
print ("\n\nDecimal a with max_mag() method : ", a.max_mag(a))

print ("Decimal a with max_mag() method : ", a.max_mag(b))

print ("Decimal b with max_mag() method : ", b.max_mag(a))
