# Python3 code to demonstrate working of
# K list Nested Dictionary Mesh
# Using * operator

# initializing lists
test_list1 = [4, 6, 8, 7]
test_list2 = [2, 7, 9, 4]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# initializing K
K = [None]

# initializing K list mesh
res = {idx: {sub2: K for sub2 in test_list2} for idx in test_list1}

# printing result
print("Created Mesh : " + str(res))
