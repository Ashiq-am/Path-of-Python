# Python Program explaining
# max() method

# loading decimal library
from decimal import *


# Initializing a decimal value
a = Decimal(-1)

b = Decimal('0.142857')

# printing Decimal values
print ("Decimal value a : ", a)
print ("Decimal value b : ", b)


# Using Decimal.max() method
print ("\n\nDecimal a with max() method : ", a.max(a))

print ("Decimal a with max() method : ", a.max(b))

print ("Decimal b with max() method : ", b.max(a))
