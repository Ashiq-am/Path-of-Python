# Python3 code to demonstrate
# Group List on K character
# using index() + list slicing

# initializing list
test_list = ['Geeks', 'for', 'M', 'Geeks', 1, 2]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 'M'

# using index() + list slicing
# Group List on K character
temp_idx = test_list.index(K)
res = [test_list[: temp_idx], test_list[temp_idx + 1: ]]

# print result
print("The list of sublist after separation : " + str(res))
