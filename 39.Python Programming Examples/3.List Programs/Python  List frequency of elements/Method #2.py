# Python3 code to demonstrate
# list frequency of elements
# using Counter() + itertools.chain.from_iterable() + map() + set()
from collections import Counter
from itertools import chain

# initializing list
test_list = [[3, 5, 4],
			[6, 2, 4],
			[1, 3, 6]]

# printing original list
print("The original list : " + str(test_list))

# using Counter() + itertools.chain.from_iterable() + map() + set()
# list frequency of elements
res = dict(Counter(chain.from_iterable(map(set, test_list))))

# printing result
print("The list frequency of elements is : " + str(res))
