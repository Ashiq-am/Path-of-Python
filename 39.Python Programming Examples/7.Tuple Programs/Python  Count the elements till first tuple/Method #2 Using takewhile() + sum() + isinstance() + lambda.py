# Python3 code to demonstrate working of
# Elements till first tuple
# using takewhile() + sum() + isinstance() + lambda
from itertools import takewhile

# initialize tuple
test_tup = (1, 5, 7, (4, 6), 10)

# printing original tuple
print("The original tuple : " + str(test_tup))

# Elements till first tuple
# using takewhile() + sum() + isinstance() + lambda
res = sum(1 for sub in takewhile(lambda ele: not isinstance(ele, tuple), test_tup))

# printing result
print("Elements till the first tuple : " + str(res))
