# Python3 code to demonstrate working of
# Check if two lists are reverse equal
# Using list slicing + "==" operator

# initializing lists
test_list1 = [5, 6, 7, 8]
test_list2 = [8, 7, 6, 5]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# Check if two lists are reverse equal
# Using list slicing + "==" operator
res = test_list1 == test_list2[::-1]

# printing result
print("Are both list reverse of each other ? : " + str(res))
