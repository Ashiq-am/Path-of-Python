# Python3 code to demonstrate
# Get match indices
# using list comprehension and enumerate()

# initializing lists
test_list1 = [5, 4, 1, 3, 2]
test_list2 = [1, 2]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# using list comprehension and enumerate()
# Get match indices
res = [key for key, val in enumerate(test_list1)
					if val in set(test_list2)]

# print result
print("The Match indices list is : " + str(res))
