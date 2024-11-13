# Python3 code to demonstrate
# set difference in dictionary list
# using itertools.filterfalse()
import itertools

# initializing list
test_list1 = [{"HpY" : 22}, {"BirthdaY" : 2}, ]
test_list2 = [{"HpY" : 22}, {"BirthdaY" : 2}, {"Shambhavi" : 2019}]

# printing original lists
print ("The original list 1 is : " + str(test_list1))
print ("The original list 2 is : " + str(test_list2))

# using itertools.filterfalse()
# set difference in dictionary list
res = list(itertools.filterfalse(lambda i: i in test_list1, test_list2)) \
	+ list(itertools.filterfalse(lambda j: j in test_list2, test_list1))

# printing result
print ("The set difference of list is : " + str(res))
