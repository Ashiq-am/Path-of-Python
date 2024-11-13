# Python3 code to demonstrate working of
# Remove K from Records
# Using list comprehension

# initializing list
test_list = [(5, 6, 7), (2, 5), (1, ), (7, 8), (9, 7, 2, 1)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 7

# Remove K from Records
# Using list comprehension
res = [tuple(ele for ele in sub if ele != K) for sub in test_list]

# printing result
print("The records after removing K : " + str(res))
