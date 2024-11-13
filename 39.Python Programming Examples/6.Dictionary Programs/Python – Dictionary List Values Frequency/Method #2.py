# Python3 code to demonstrate working of
# Dictionary List Values Frequency
# Using chain.from_iterables() + Counter()
from collections import Counter
from itertools import chain

# initializing dictionary
test_dict = {1: ['gfg', 'best', 'geeks'],
             2: ['gfg', 'CS'],
             3: ['best', 'for', 'CS'],
             4: ['test', 'ide', 'success'],
             5: ['gfg', 'is', 'best']}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Dictionary List Values Frequency
# Using chain.from_iterables() + Counter()
res = Counter(chain.from_iterable(test_dict.values()))

# printing result
print("Values Frequency : " + str(dict(res)))
