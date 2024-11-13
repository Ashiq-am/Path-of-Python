# Python3 code to demonstrate
# shuffle a tuple
# using random.shuffle()
import random

# initializing tuple
tup = (1,2,3,4,5)

# Printing original tuple
print("The original tuple is : " + str(tup))

# Conversion to list
l = list(tup)

# using random.shuffle()
# to shuffle a list
random.shuffle(l)

# Converting back to tuple
tup = tuple(l)

# Printing shuffled tuple
print ("The shuffled tuple is : " + str(tup))
