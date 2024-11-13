# import Decimal function from
# decimal library
from decimal import Decimal
print(Decimal("0.1"))
print(Decimal(0.1))

# Rounding a Decimal number is
# done with the .quantize() function
# "1.0" in .quantize() determines the
# number of decimal places to round the number
print(Decimal("1.65").quantize(Decimal("1.0")))
print(Decimal("1.675").quantize(Decimal("1.00")))
