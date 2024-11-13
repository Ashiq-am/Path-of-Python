# Python3 code to demonstrate
# Matching elements count
# using list comprehension and enumerate() + len()

# initializing lists
test_list1 = [5, 4, 1, 3, 2]
test_list2 = [1, 2]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# using list comprehension and enumerate() + len()
# Matching elements count
res = len([key for key, val in enumerate(test_list1) if val in set(test_list2)])

# print result
print("The Match indices list count is : " + str(res))
