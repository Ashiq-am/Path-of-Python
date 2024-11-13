# Python3 code to demonstrate working of
# Nested Dictionary values summation
# Using Counter() + values()
from collections import Counter

# initializing dictionary
test_dict = {'gfg': {'a': 4, 'b': 5, 'c': 8},
             'is': {'a': 8, 'c': 10},
             'best': {'c': 19, 'b': 10}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Nested Dictionary values summation
# Using Counter() + values()
res = Counter()
for val in test_dict.values():
    res.update(val)

# printing result
print("The summation dictionary is : " + str(dict(res)))
