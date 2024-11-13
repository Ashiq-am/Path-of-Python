# Python3 code to demonstrate
# filter repeated tuple
# using list comprehension

# initializing lists
test_list1 = [('Geeks', 'for'), ('Geeks', 'is'), ('Computer', 'Science')]
test_list2 = [('Geeks', 'for'), ('Geeks', 'is')]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 1 : " + str(test_list2))

# using list comprehension
# filter repeated tuple
res = [sub for sub in test_list1 if sub not in test_list2]

# print result
print("The filtered list of tuples : " + str(res))
