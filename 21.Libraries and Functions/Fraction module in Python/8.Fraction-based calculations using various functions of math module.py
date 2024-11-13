import math
from fractions import Fraction

print (math.sqrt(Fraction(25, 4)))
# returns 2.5

print (math.sqrt(Fraction(28,3)))
# returns 3.0550504633038935

print (math.floor(Fraction(3558, 1213)))
# returns 2

print (Fraction(math.sin(math.pi/3)))
# returns Fraction(3900231685776981, 4503599627370496)

print (Fraction(math.sin(math.pi/3)).limit_denominator(10))
# returns Fraction(6, 7)
