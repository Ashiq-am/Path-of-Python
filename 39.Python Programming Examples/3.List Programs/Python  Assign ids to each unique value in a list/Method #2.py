# Python3 code to demonstrate
# assigning ids to values using
# list comprehension + OrderedDict.fromkeys() + enumerate()
from collections import OrderedDict

# initializing list
test_list = [5, 6, 7, 6, 5, 1]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + OrderedDict.fromkeys() + enumerate()
# assigning ids to values
res = [{val : key for key, val in enumerate(
		OrderedDict.fromkeys(test_list))}
				[ele] for ele in test_list]

# print result
print("The ids of assigned values is : " + str(res))
