# Python Program explaining
# quantize() method

# loading decimal library
from decimal import *


# Initializing a decimal value
a = Decimal(-1)

b = Decimal('0.142857')

# printing Decimal values
print ("Decimal value a : ", a)
print ("Decimal value b : ", b)


# Using Decimal.quantize() method
print ("\n\nDecimal a with quantize() method : ", a.quantize(b))

print ("Decimal b with quantize() method : ", b.quantize(b))
