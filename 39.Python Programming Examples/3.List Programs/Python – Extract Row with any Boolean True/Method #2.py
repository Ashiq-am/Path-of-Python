# Python3 code to demonstrate working of
# Extract Row with any Boolean True
# Using any() + filter() + lambda

# initializing list
test_list = [[False, False], [True, True, True], [False, True], [False]]

# printing original list
print("The original list is : " + str(test_list))

# using any() to check for any True value
# filter() to perform filtering
res = list(filter(lambda sub : any(ele for ele in sub), test_list))

# printing result
print("Extracted Rows : " + str(res))
