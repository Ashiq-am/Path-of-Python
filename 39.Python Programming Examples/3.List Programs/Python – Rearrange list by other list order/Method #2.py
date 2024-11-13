# Python3 code to demonstrate working of
# Rearrange list by other list order
# Using sorted + index()

# initializing lists
test_list1 = [5, 6, 7, 4, 8, 9, 2]
test_list2 = [9, 6, 4]

# printing original list
print("The original list 1 is : " + str(test_list1))

# printing original list
print("The original list 2 is : " + str(test_list2))

# Rearrange list by other list order
# Using sorted + index()
res = sorted(test_list2, key = test_list1.index)

# printing result
print("The list after sorting is : " + str(res))
