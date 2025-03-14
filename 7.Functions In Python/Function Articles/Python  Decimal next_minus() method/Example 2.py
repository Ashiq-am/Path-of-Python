# Python Program explaining
# next_minus() method

# loading decimal library
from decimal import *


# Initializing a decimal value
a = Decimal('-3.14')

b = Decimal('321e + 5')

# printing Decimal values
print ("Decimal value a : ", a)
print ("Decimal value b : ", b)


# Using Decimal.next_minus() method
print ("\n\nDecimal a with next_minus() method : ", a.next_minus())

print ("Decimal a with next_minus() method : ", a.next_minus())

print ("Decimal b with next_minus() method : ", b.next_minus())
