# Python3 code to demonstrate working of
# Append Dictionary Keys and Values ( In order ) in dictionary
# Using chain() + keys() + values()
from itertools import chain

# initializing dictionary
test_dict = {"Gfg" : 1, "is" : 3, "Best" : 2}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# chain() is used for concatenation
res = list(chain(test_dict.keys(), test_dict.values()))

# printing result
print("The ordered keys and values : " + str(res))
