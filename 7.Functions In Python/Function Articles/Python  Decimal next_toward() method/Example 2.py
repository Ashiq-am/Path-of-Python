# Python Program explaining
# next_toward() method

# loading decimal library
from decimal import *


# Initializing a decimal value
a = Decimal('-3.14')

b = Decimal('321e + 5')


# printing Decimal values
print ("Decimal value a : ", a)
print ("Decimal value b : ", b)


# Using Decimal.next_toward() method
print ("\n\nDecimal a with next_toward() method : ", a.next_toward(b))

print ("Decimal b with next_toward() method : ", b.next_toward(b))
