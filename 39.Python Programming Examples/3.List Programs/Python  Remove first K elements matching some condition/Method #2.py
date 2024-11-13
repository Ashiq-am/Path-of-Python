# Python3 code to demonstrate
# to remove first K elements matching condition
# using itertools.filterfalse() + itertools.count()
from itertools import filterfalse, count

# initializing list
test_list = [3, 5, 1, 6, 7, 9, 8, 5]

# printing original list
print ("The original list is : " + str(test_list))

# using itertools.filterfalse() + itertools.count()
# to remove first K elements matching condition
# removes first 4 odd occurrences
res = filterfalse(lambda i, counter = count(): i % 2 != 0 and
								next(counter) < 4, test_list)

# printing result
print ("The filtered list is : " + str(list(res)))
