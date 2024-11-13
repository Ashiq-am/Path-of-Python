# Python3 code to demonstrate
# Flatten and Reverse Sort Matrix
# using sorted + list comprehension

# initializing list of list
test_list = [[3, 5], [7, 3, 9], [1, 12]]

# printing original list of list
print("The original list : " + str(test_list))

# using sorted + list comprehension
# Flatten and Reverse Sort Matrix
res = sorted([j for i in test_list for j in i], reverse = True)

# print result
print("The reverse sorted and flattened list : " + str(res))
