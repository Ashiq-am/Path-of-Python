# Python3 code to demonstrate working of
# Dictionary Values Frequency
# Using defaultdict() + loop
from collections import defaultdict

# initializing dictionary
test_dict = {'ide': 3, 'Gfg': 3, 'code': 2}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Dictionary Values Frequency
# Using defaultdict() + loop
res = defaultdict(int)
for key, val in test_dict.items():
    res[val] += 1

# printing result
print("The frequency dictionary : " + str(dict(res)))
