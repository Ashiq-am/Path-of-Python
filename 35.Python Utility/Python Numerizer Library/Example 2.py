# Importing Numerize function
# From Numerizer Library
from numerizer import numerize


# here we can also pass numerical
# values with corresponding periods
# it will still give same output
a = numerize('320 thousand three hundred twenty ')
print(a)

a = numerize('990 trillion 988 billion 881 million 999 thousand nine hundred ninety nine')
print(a)

# here we can also get float values
# in our output by using "half" and
# "quarter" terms in input
a = numerize('twenty nine one half')
print(a)
type(a)

# here we are explicitly converting
# our output into float type
a = float(numerize(' nine hundred ninety and two half'))

# it will add two half
# (i.e. 1/2+1/2) to our no
# which will add 1 to our answer
print(a)
type(a)

a = numerize('two thousand four hundred twenty and three quarters')

# it will add (3/4) to our answer
print(a)
