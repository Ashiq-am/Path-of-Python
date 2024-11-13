# Python3 code to demonstrate working of
# Difference in Record Lists
# Using set.intersection() + set operations

# Initializing lists
test_list1 = [('gfg', 1), ('is', 2), ('best', 3)]
test_list2 = [('i', 3), ('love', 4), ('gfg', 1)]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Difference in Record Lists
# Using set.intersection() + set operations
res = list(set(test_list1).intersection(set(test_list2)))
res = list(set(res) ^ set(test_list1))

# printing result
print("The difference of data records is : " + str(res))
