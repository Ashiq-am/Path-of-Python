# Python3 code to demonstrate
# Matrix elements Frequencies Counter
# using Counter() + chain()
from collections import Counter
import itertools

# Initializing list
test_list = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]

# printing original list
print("The original list is : " + str(test_list))

# Matrix elements Frequencies Counter
# using Counter() + chain()
res = dict(Counter(itertools.chain(*test_list)))

# printing result
print ("The frequencies dictionary is : " + str(res))
