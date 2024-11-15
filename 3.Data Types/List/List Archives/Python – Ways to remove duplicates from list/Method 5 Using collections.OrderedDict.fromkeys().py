# Python 3 code to demonstrate
# removing duplicated from list
# using collections.OrderedDict.fromkeys()
from collections import OrderedDict

# initializing list
test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print ("The original list is : " + str(test_list))

# using collections.OrderedDict.fromkeys()
# to remove duplicated
# from list
res = list(OrderedDict.fromkeys(test_list))

# printing list after removal
print ("The list after removing duplicates : " + str(res))
