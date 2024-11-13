# Importing Numerize function
# From Numerizer Library
from numerizer import numerize


# We can get interger value
# in output by converting explicitly
a = int(numerize('Three'))
print(a)
print(numerize('five thousand two hundred and twenty'))


# If we are not converting our
# output explicitly into integer
# then by default it will return
# a string value
a = numerize('forty four thousand four hundred forty four')
print(a)
print("Type", type(a))

a = numerize('sixty billion forty million twenty thousand four hundred six')
print(a)
