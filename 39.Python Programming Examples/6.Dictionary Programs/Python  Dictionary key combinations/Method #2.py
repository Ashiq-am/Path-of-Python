# Python3 code to demonstrate working of
# Dictionary key combinations
# Using itertools.combinations()
import itertools

# Initializing dict
test_dict = {'gfg' : 1, 'is' : 2, 'the' : 3, 'best' : 4}

# printing original dict
print("The original dict is : " + str(test_dict))

# Dictionary key combinations
# Using itertools.combinations()
res = list(itertools.combinations(test_dict, 2))

# printing result
print("The dictionary key pair list is : " + str(res))
