# Python3 code to demonstrate working of
# Test if element is part of dictionary
# Using chain.from_iterables() + items()
from itertools import chain

# initializing dictionary
test_dict = {"Gfg" : 1, "is" : 3, "Best" : 2}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing K
K = "Gfg"

# flattening key-values and then checking
# using in operator
res = K in chain.from_iterable(test_dict.items())

# printing result
print("Is K present in dictionary? : " + str(res))
