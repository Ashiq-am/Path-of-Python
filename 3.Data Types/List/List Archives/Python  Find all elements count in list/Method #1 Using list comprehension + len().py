# Python3 code to demonstrate
# count of all the elements in list
# Using list comprehension

# initializing list
test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension
# count of all the elements in list
res = len([ele for sub in test_list for ele in sub])

# print result
print("The total element count in lists is : " + str(res))
