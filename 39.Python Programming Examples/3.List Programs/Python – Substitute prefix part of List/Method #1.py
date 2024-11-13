# Python3 code to demonstrate working of
# Substitute prefix part of List
# Using len() + list slicing

# initializing lists
test_list1 = [4, 6, 8, 7]
test_list2 = [2, 7, 9, 4, 2, 8, 6, 4, 1, 10]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# size slicing after length of list 1
res = test_list1 + test_list2[len(test_list1) : ]

# printing result
print("The joined list : " + str(res))
