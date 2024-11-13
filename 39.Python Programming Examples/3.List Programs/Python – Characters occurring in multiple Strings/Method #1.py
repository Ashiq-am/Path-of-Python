# Python3 code to demonstrate working of
# Characters occurring in multiple Strings
# Using Counter() + set()
from itertools import chain
from collections import Counter

# initializing list
test_list = ['gfg', 'is', 'best', 'for', 'geeks', 'and', 'cs']

# printing original list
print("The original list is : " + str(test_list))

# Characters occurring in multiple Strings
# Using Counter() + set()
temp = (set(sub) for sub in test_list)
cntr = Counter(chain.from_iterable(temp))
res = [chr for chr, count in cntr.items() if count >= 2]

# printing result
print("Characters with Multiple String occurrence : " + str(res))
