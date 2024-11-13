from fractions import Fraction

print (Fraction('3.14159265358979323846'))
# returns Fraction(157079632679489661923, 50000000000000000000)

print (Fraction('3.14159265358979323846').limit_denominator(10000))
# returns Fraction(355, 113)

print (Fraction('3.14159265358979323846').limit_denominator(100))
# returns Fraction(311, 99)

print (Fraction('3.14159265358979323846').limit_denominator(10))
# returns Fraction(22, 7)

print (Fraction(125, 50).numerator)
# returns 5

print (Fraction(125, 50).denominator)
# returns 2
