# Python Program explaining
# next_plus() method

# loading decimal library
from decimal import *


# Initializing a decimal value
a = Decimal(-1)

b = Decimal('0.142857')

# printing Decimal values
print ("Decimal value a : ", a)
print ("Decimal value b : ", b)


# Using Decimal.next_plus() method
print ("\n\nDecimal a with next_plus() method : ", a.next_plus())

print ("Decimal a with next_plus() method : ", a.next_plus())

print ("Decimal b with next_plus() method : ", b.next_plus())
