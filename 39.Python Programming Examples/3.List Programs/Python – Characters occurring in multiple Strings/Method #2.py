# Python3 code to demonstrate working of
# Characters occurring in multiple Strings
# Using list comprehension + Counter() + set()
from itertools import chain
from collections import Counter

# initializing list
test_list = ['gfg', 'is', 'best', 'for', 'geeks', 'and', 'cs']

# printing original list
print("The original list is : " + str(test_list))

# Characters occurring in multiple Strings
# Using list comprehension + Counter() + set()
res = [key for key, val in Counter([ele for sub in test_list
                                    for ele in set(sub)]).items()
       if val > 1]

# printing result
print("Characters with Multiple String occurrence : " + str(res))
