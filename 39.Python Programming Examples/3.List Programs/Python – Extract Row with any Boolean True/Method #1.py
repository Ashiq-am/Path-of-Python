# Python3 code to demonstrate working of
# Extract Row with any Boolean True
# Using list comprehension + any()

# initializing list
test_list = [[False, False], [True, True, True], [False, True], [False]]

# printing original list
print("The original list is : " + str(test_list))

# using any() to check for any True value
res = [sub for sub in test_list if any(ele for ele in sub)]

# printing result
print("Extracted Rows : " + str(res))
