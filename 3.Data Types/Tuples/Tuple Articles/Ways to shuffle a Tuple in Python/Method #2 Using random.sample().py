# Python3 code to demonstrate
# shuffle a tuple
# using random.sample()
import random

# initializing tuple
tup = (1,2,3,4,5)

# Printing original tuple
print("The original tuple is : " + str(tup))

# Using random.sample(), passing the tuple and
# the length of the datastructure as arguments
# and converting it back to tuple.
tup = tuple(random.sample(t, len(t)))

# Printing shuffled tuple
print ("The shuffled tuple is : " + str(tup))
