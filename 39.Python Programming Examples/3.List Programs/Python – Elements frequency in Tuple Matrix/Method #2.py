# Python3 code to demonstrate working of
# Elements frequency in Tuple Matrix
# Using chain.from_iterables() + Counter()
from itertools import chain
from collections import Counter

# initializing lists
test_list = [[(4, 5), (3, 2)], [(2, 2)], [(1, 2), (5, 5)]]

# printing original list
print("The original list is : " + str(test_list))

# Elements frequency in Tuple Matrix
# Using chain.from_iterables() + Counter()
res = dict(Counter(chain.from_iterable(chain.from_iterable(test_list))))

# printing result
print("Elements frequency : " + str(res))
