# Python3 code to demonstrate working of
# Elements frequency in Tuple Matrix
# Using nested chain() + "*" operator + Counter()
from itertools import chain
from collections import Counter

# initializing lists
test_list = [[(4, 5), (3, 2)], [(2, 2)], [(1, 2), (5, 5)]]

# printing original list
print("The original list is : " + str(test_list))

# Elements frequency in Tuple Matrix
# Using nested chain() + "*" operator + Counter()
res = dict(Counter(chain(*chain(*test_list))))

# printing result
print("Elements frequency : " + str(res))
