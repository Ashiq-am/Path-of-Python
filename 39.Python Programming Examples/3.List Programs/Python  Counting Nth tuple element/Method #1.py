# Python3 code to demonstrate working of
# Counting Nth tuple element
# using Counter() + generator expression
from collections import Counter

# initialize list
test_list = [('gfg', 0), ('is', 1), ('best', 2),
			('gfg', 2), ('is', 0), ('for', 1),
			('geeks', 2)]

# printing original list
print("The original list : " + str(test_list))

# initialize N
N = 1

# Counting Nth tuple element
# using Counter() + generator expression
res = dict(Counter(sub[N] for sub in test_list))

# printing result
print("The grouped Nth element frequency is : " + str(res))
