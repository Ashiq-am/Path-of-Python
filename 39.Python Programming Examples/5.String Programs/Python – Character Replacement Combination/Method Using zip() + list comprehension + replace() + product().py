# Python3 code to demonstrate working of
# Character Replacement Combination
# Using zip() + list comprehension + replace() + product()
from itertools import product

# initializing string
test_str = "geeks"

# printing original string
print("The original string is : " + str(test_str))

# initializing dictionary
test_dict = {'s': ['1', '2'], 'k': ['3']}

# adding original character to possible characters
for key in test_dict.keys():
    if key not in test_dict[key]:
        test_dict[key].append(key)

res = []

# constructing all possible combination of values using product
# mapping using zip()
for sub in [zip(test_dict.keys(), chr) for chr in product(*test_dict.values())]:
    temp = test_str
    for repls in sub:
        # replacing all elements at once using * operator
        temp = temp.replace(*repls)
    res.append(temp)

# printing result
print("All combinations : " + str(res))
