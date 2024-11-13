# Python3 code to demonstrate working of
# Check if elements index are equal for list elements
# Using zip() + all() + generator expression

# initializing lists
test_list1 = [2, 6, 9, 7, 8]
test_list2 = [2, 7, 9, 4, 8]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# initializing check_list
check_list = [9, 8, 2]

# checking for all elements equal in check list using all()
res = all(a == b for a, b in zip(test_list1, test_list2) if a in check_list)

# printing result
print("Are elements at same index for required instances ?: " + str(res))
