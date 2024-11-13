# Python3 code to demonstrate working of
# Filter rows with required elements
# Using list comprehension + all()

# initializing list
test_list = [[2, 4, 6], [7, 4, 3, 2], [2, 4, 8], [1, 1, 9]]

# printing original list
print("The original list is : " + str(test_list))

# initializing check_list
check_list = [4, 6, 2, 8]

# using in operator to check for presence
res = [sub for sub in test_list if all(ele in check_list for ele in sub)]

# printing result
print("Filtered rows : " + str(res))
