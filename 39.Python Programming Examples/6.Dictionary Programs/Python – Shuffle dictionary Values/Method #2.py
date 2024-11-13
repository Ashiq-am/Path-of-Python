# Python3 code to demonstrate working of
# Shuffle dictionary Values
# Using sample() + zip()
from random import sample

# initializing dictionary
test_dict = {"gfg": 1, "is": 7, "best": 8,
			"for": 3, "geeks": 9}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# reassigning to keys
res = dict(zip(test_dict, sample(list(test_dict.values()),
								len(test_dict))))

# printing result
print("The shuffled dictionary : " + str(res))
