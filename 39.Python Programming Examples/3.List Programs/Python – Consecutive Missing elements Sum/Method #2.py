# Python3 code to demonstrate
# Consecutive Missing elements Sum
# Using set() + sum()

# initializing list
test_list = [3, 5, 6, 8, 10]

# printing original list
print("The original list : " + str(test_list))

# Using set() + sum()
# Consecutive Missing elements Sum
res = sum(list(set(range(max(test_list) + 1)) - set(test_list)))

# print result
print("The sum of missing elements : " + str(res))
