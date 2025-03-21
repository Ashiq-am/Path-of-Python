# Python3 code to demonstrate working of
# Retain all K elements Rows
# Using list comprehension + any()

# initializing list
test_list = [[2, 4, 6], [2, 2, 2], [2, 3], [2, 2]]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 2

# Retain all K elements Rows
# Using list comprehension + any()
res = [ele for ele in test_list if not any(el != K for el in ele)]

# printing result
print("Matrix after filtering : " + str(res))
