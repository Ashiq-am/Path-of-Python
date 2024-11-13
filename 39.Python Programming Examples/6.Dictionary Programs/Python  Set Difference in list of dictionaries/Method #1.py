# Python3 code to demonstrate
# set difference in dictionary list
# using list comprehension

# initializing list
test_list1 = [{"HpY" : 22}, {"BirthdaY" : 2}, ]
test_list2 = [{"HpY" : 22}, {"BirthdaY" : 2}, {"Shambhavi" : 2019}]

# printing original lists
print ("The original list 1 is : " + str(test_list1))
print ("The original list 2 is : " + str(test_list2))

# using list comprehension
# set difference in dictionary list
res = [i for i in test_list1 if i not in test_list2] \
	+ [j for j in test_list2 if j not in test_list1]

# printing result
print ("The set difference of list is : " + str(res))
