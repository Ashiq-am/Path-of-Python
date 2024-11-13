# Python3 code to demonstrate
# Consecutive Missing elements Sum
# using list comprehension + sum()

# initializing list
test_list = [3, 5, 6, 8, 10]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + sum()
# Consecutive Missing elements Sum
res = sum([ele for ele in range(max(test_list) + 1) if ele not in test_list])

# print result
print("The sum of missing elements : " + str(res))
