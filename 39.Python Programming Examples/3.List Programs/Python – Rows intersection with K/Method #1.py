# Python3 code to demonstrate working of
# Rows intersection with K
# Using sum() + generator expression

# initializing lists
test_list1 = [[5, 6, 7], [7, 6, 6], [5, 7, 10]]
test_list2 = [[5, 6, 7], [7, 6, 8], [5, 7, 10]]

# printing original list
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# initializing K
K = 5

# Rows intersection with K
# Using sum() + generator expression
res = sum(sum(a == b for b in test_list2) for a in test_list1 if K in a)

# printing result
print("The matched rows : " + str(res))
