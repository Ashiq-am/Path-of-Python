# Python3 code to demonstrate
# Matrix elements Frequencies Counter
# using Counter() + sum() + map()
from collections import Counter

# Initializing list
test_list = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]

# printing original list
print("The original list is : " + str(test_list))

# Matrix elements Frequencies Counter
# using Counter() + sum() + map()
res = dict(sum(map(Counter, test_list), Counter()))

# printing result
print ("The frequencies dictionary is : " + str(res))
