# Python Program explaining
# min() method

# loading decimal library
from decimal import *


# Initializing a decimal value
a = Decimal('-3.14')

b = Decimal('321e + 5')

# printing Decimal values
print ("Decimal value a : ", a)
print ("Decimal value b : ", b)


# Using Decimal.min() method
print ("\n\nDecimal a with min() method : ", a.min(a))

print ("Decimal a with min() method : ", a.min(b))

print ("Decimal b with min() method : ", b.min(a))
