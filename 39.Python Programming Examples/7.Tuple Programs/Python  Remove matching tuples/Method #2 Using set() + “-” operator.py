# Python3 code to demonstrate
# filter repeated tuple
# using set() + "-" operator

# initializing lists
test_list1 = [('Geeks', 'for'), ('Geeks', 'is'), ('Computer', 'Science')]
test_list2 = [('Geeks', 'for'), ('Geeks', 'is')]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 1 : " + str(test_list2))

# using set() + "-" operator
# filter repeated tuple
res = list(set(test_list1) - set(test_list2))

# print result
print("The filtered list of tuples : " + str(res))
