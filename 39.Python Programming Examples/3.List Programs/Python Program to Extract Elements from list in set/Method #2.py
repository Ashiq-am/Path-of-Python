# Python3 code to demonstrate working of
# Elements from list in set
# Using repeat() + from_iterable() + count()
from itertools import chain, repeat

# initializing list
test_list = [5, 6, 2, 3, 2, 6, 5, 8, 9]

# printing original list
print("The original list is : " + str(test_list))

# initializing search set
search_set = {6, 2, 8}

# repeat repeats all the occurrences of elements
res = list(chain.from_iterable((repeat(ele, test_list.count(ele))
                                for ele in search_set)))

# printing result
print("Set present list elements : " + str(res))
