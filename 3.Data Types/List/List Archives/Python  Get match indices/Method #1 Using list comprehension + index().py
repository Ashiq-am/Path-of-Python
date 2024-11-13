# Python3 code to demonstrate
# Get match indices
# using list comprehension and index()

# initializing lists
test_list1 = [5, 4, 1, 3, 2]
test_list2 = [1, 2]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# using list comprehension and index()
# Get match indices
res = [test_list1.index(i) for i in test_list2]

# print result
print("The Match indices list is : " + str(res))
