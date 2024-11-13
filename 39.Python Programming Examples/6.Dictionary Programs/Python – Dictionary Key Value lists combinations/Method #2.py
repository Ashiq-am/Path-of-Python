# Python3 code to demonstrate working of
# Dictionary Key Value lists combinations
# Using product() + loop
from itertools import product

# initializing dictionary
test_dict = {"Gfg": [4, 5, 7],
             "is": [1, 2, 9],
             "Best": [9, 4, 2]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

res = {}
for key, val in test_dict.items():
    # for key-value combinations
    res[key] = product([key], val)

# computing cross key combinations
res = product(*res.values())

# printing result
print("The computed combinations : " + str(list(res)))
