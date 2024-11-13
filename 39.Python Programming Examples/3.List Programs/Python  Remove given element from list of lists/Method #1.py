# Python3 code to demonstrate
# Removing element from list of lists
# using list comprehension

# initializing list
test_list = [[4, 5, 6], [5, 6, 4, 1], [4], [4, 8, 9, 10]]

# printing original list
print("The original list : " + str(test_list))

# initializing Number to delete
N = 4

# using list comprehension
# Removing element from list of lists
res = [[ele for ele in sub if ele != N] for sub in test_list]

# print result
print("The list after deletion of element : " + str(res))
