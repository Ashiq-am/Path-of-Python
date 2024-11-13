# Python3 code to demonstrate working of
# Symmetric Difference of Multiple sets
# Using Counter() + chain.from_iterable() + items()
from collections import Counter
from itertools import chain

# initializing list
test_list = [{5, 3, 2, 6, 1},
             {7, 5, 3, 8, 2},
             {9, 3}, {0, 3, 6, 7}]

# printing original list
print("The original list is : " + str(test_list))

# clubbing operations using items() to get items
res = {key for key, val in Counter(chain.
                                   from_iterable(test_list)).
    items() if val == 1}

# printing result
print("Symmetric difference of multiple list : " + str(res))
