# Python Program illustrating
# numpy.all() method

import numpy as geek

# Axis = NULL
# True False
# True True
# True : False = False

print("Bool Value with axis = NONE : ", geek.all([[True,False],[True,True]]))

# Axis = 0
# True False
# True True
# True : False
print("\nBool Value with axis = 0 : ", geek.all([[True,False],[True,True]], axis = 0))

print("\nBool : ", geek.all([-1, 4, 5]))


# Not a Number (NaN), positive infinity and negative infinity
# evaluate to True because these are not equal to zero.
print("\nBool : ", geek.all([1.0, geek.nan]))

print("\nBool Value : ", geek.all([[0, 0],[0, 0]]))
