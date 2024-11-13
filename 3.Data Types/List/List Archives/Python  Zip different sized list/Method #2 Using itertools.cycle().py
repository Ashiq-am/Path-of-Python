# Python3 code to demonstrate
# zipping of two different size list
# using itertools.cycle()
from itertools import cycle

# initializing lists
test_list1 = [7, 8, 4, 5, 9, 10]
test_list2 = [1, 5, 6]

# printing original lists
print ("The original list 1 is : " + str(test_list1))
print ("The original list 2 is : " + str(test_list2))

# using itertools.cycle()
# zipping of two different size list
res = list(zip(test_list1, cycle(test_list2))
			if len(test_list1) > len(test_list2)
			else zip(cycle(test_list1), test_list2))

# printing result
print ("The zipped list is : " + str(res))
