# Python3 code to demonstrate working of
# Rearrange dictionary for consective value-keys
# Using dictionary comprehension + accumulate()
from itertools import accumulate

# initializing dictionary
test_dict = {1 : 3, 4 : 5, 3 : 4, 5 : 6}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Rearrange dictionary for consective value-keys
# Using dictionary comprehension + accumulate()
res = {key : test_dict[key] for key in accumulate(test_dict,
							lambda key, x :test_dict[key])}

# printing result
print("The rearranged dictionary : " + str(res))
