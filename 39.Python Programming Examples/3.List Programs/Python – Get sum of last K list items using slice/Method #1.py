# Python3 code to demonstrate
# Inverse K slice Sum
# using list slicing + sum()

# initializing list
test_list = [4, 5, 2, 6, 7, 8, 10]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 5

# Inverse K slice Sum
# using list slicing + sum()
res = sum(test_list[-K:])

# print result
print("The last K elements sum of list is : " + str(res))
