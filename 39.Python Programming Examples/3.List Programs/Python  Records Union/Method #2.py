# Python3 code to demonstrate working of
# Records Union
# Using set.union()

# Initializing lists
test_list1 = [('gfg', 1), ('is', 2), ('best', 3)]
test_list2 = [('i', 3), ('love', 4), ('gfg', 1)]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Records Union
# set.union()
res = list(set(test_list1).union(set(test_list2)))

# printing result
print("The union of data records is : " + str(res))
