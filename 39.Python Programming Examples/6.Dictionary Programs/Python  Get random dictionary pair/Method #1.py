# Python3 code to demonstrate working of
# Get random dictionary pair in dictionary
# Using random.choice() + list() + items()
import random

# Initialize dictionary
test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Get random dictionary pair in dictionary
# Using random.choice() + list() + items()
res = key, val = random.choice(list(test_dict.items()))

# printing result
print("The random pair is : " + str(res))
