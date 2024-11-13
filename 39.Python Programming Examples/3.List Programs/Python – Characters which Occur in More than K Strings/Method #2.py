# Python3 code to demonstrate
# Characters which Occur in More than K Strings
# using set() + Counter() + dictionary comprehension
from collections import Counter

# Initializing list
test_list = ['Gfg', 'ise', 'for', 'Geeks']

# printing original list
print("The original list is : " + str(test_list))

# Initializing K
K = 2

# Characters which Occur in More than K Strings
# using set() + Counter() + dictionary comprehension
res = {key for key, val in Counter([ele for sub in
                                    test_list for ele in set(sub)]).items()
       if val >= K}

# printing result
print("Filtered Characters are : " + str(res))
