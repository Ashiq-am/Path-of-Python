# Python3 code to demonstrate working of
# Inverse Dictionary Values List
# Using
from collections import defaultdict

# initializing dictionary
test_dict = {1: [2, 3], 2: [3], 3: [1], 4: [2, 1]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing empty list as Values
res = defaultdict(list)

# using loop to perform reverse mapping
for keys, vals in test_dict.items():
    for val in vals:
        res[val].append(keys)

# printing result
print("The required result : " + str(dict(res)))
