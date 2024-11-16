# Python Program illustrating
# numpy.any() method

import numpy as geek

# Axis = NULL
# True False
# True True
# True : False = True (OR)

print("Bool Value with axis = NONE : ", geek.any([[True,False],[True,True]]))

# Axis = 0
# True False
# True True
# True : False
print("\nBool Value with axis = 0 : ", geek.any([[True,False],[True,True]], axis = 0))

print("\nBool : ", geek.any([-1, 4, 5]))


# Not a Number (NaN), positive infinity and negative infinity
# evaluate to True because these are not equal to zero.
print("\nBool : ", geek.any([1.0, geek.nan]))

print("\nBool Value : ", geek.any([[0, 0],[0, 0]]))
