# Python3 code to demonstrate working of
# Counting Nth tuple element
# using Counter() + map() + itemgetter()
from collections import Counter
from operator import itemgetter

# initialize list
test_list = [('gfg', 0), ('is', 1), ('best', 2),
			('gfg', 2), ('is', 0), ('for', 1),
			('geeks', 2)]

# printing original list
print("The original list : " + str(test_list))

# initialize N
N = 1

# Counting Nth tuple element
# using Counter() + map() + itemgetter()
res = dict(Counter(map(itemgetter(N), test_list)))

# printing result
print("The grouped Nth element frequency is : " + str(res))
