# Python3 code to demonstrate
# assign unique value to list elements
# using setdefault() + map() + count()
from itertools import count

# initializing list
test_list = [1, 4, 6, 1, 4, 5, 6]

# printing the original list
print ("The original list is : " + str(test_list))

# using setdefault() + map() + count()
# assign unique value to list elements
res = list(map({}.setdefault, test_list, count()))

# printing result
print ("The unique value list is : " + str(res))
