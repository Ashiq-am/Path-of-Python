# Python3 code to demonstrate working of
# Concatenate All Records
# using join() + map() + chain.from_iterable()
from itertools import chain

# initialize list
test_list = [('geeksforgeeks ', 'is' ), (' best', ' for'), (' all', ' geeks')]

# printing original list
print("The original list : " + str(test_list))

# Concatenate All Records
# using join() + map() + chain.from_iterable()
res = "".join(map(str, chain.from_iterable(test_list)))

# printing result
print("The Concatenated elements of list is : " + str(res))
