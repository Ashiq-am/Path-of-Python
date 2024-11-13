# Python3 code to demonstrate working of
# Record elements count
# using len() + map() + chain.from_iterable()
from itertools import chain

# initialize list
test_list = [(2, 4), (6, 7), (5, 1), (6, 10), (8, 7)]

# printing original list
print("The original list : " + str(test_list))

# Record elements count
# using len() + map() + chain.from_iterable()
res = len(list((map(int, chain.from_iterable(test_list)))))

# printing result
print("The total count of list is : " + str(res))
