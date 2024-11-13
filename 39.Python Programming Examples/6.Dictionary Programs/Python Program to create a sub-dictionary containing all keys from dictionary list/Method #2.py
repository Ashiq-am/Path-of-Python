# Python3 code to demonstrate working of
# Ensure all keys in dictionary list
# Using set() + chain.from_iterable() + update()
from itertools import chain

# initializing list
test_list = [{'gfg': 3, 'is': 7},
             {'gfg': 3, 'is': 1, 'best': 5},
             {'gfg': 8}]

# printing original list
print("The original list is : " + str(test_list))

# extracting all keys
all_keys = set(chain.from_iterable(test_list))

# assigning None using update() if key is not found
for sub in test_list:
    sub.update({key: None for key in all_keys if key not in sub})

# printing result
print("Reformed dictionaries list : " + str(test_list))
