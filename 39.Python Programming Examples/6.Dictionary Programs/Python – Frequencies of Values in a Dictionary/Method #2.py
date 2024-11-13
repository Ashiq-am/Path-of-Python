# Python3 code to demonstrate working of
# Dictionary Values Frequency
# Using Counter() + values()
from collections import Counter

# initializing dictionary
test_dict = {'ide': 3, 'Gfg': 3, 'code': 2}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Dictionary Values Frequency
# Using defaultdict() + loop
res = Counter(test_dict.values())

# printing result
print("The frequency dictionary : " + str(dict(res)))
