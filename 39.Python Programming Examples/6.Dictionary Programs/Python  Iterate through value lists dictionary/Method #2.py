# Python3 code to demonstrate working of
# Iterating through value lists dictionary
# Using from_iterable() + product() + items()
import itertools

# Initialize dictionary
test_dict = {'gfg': [1, 2], 'is': [4, 5], 'best': [7, 8]}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Iterating through value lists dictionary
# Using from_iterable() + product() + items()
res = []
for key, value in (itertools.chain.from_iterable
    ([itertools.product((k,), v) for k, v in test_dict.items()])):
    res.append(value)

# printing result
print("The list values of keys are : " + str(res))
