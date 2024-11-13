# Python3 code to demonstrate working of
# Dictionary List Values Frequency
# Using loop + defaultdict()
from collections import defaultdict

# initializing dictionary
test_dict = {1: ['gfg', 'best', 'geeks'],
             2: ['gfg', 'CS'],
             3: ['best', 'for', 'CS'],
             4: ['test', 'ide', 'success'],
             5: ['gfg', 'is', 'best']}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Dictionary List Values Frequency
# Using loop + defaultdict()
res = defaultdict(int)
for key, val in test_dict.items():
    for sub in val:
        res[sub] += 1

# printing result
print("Values Frequency : " + str(dict(res)))
