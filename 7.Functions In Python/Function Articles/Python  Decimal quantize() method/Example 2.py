# Python Program explaining
# quantize() method

# loading decimal library
from decimal import *


# Initializing a decimal value
a = Decimal('-3.14')

b = Decimal('321e + 5')


# printing Decimal values
print ("Decimal value a : ", a)
print ("Decimal value b : ", b)


# Using Decimal.quantize() method
print ("\n\nDecimal a with quantize() method : ", a.quantize(b))

print ("Decimal b with quantize() method : ", b.quantize(b))
