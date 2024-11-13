# Python3 code to demonstrate
# Finding missing elements in List
# Using set()

# initializing list
test_list = [3, 5, 6, 8, 10]

# printing original list
print("The original list : " + str(test_list))

# Using set()
# Finding missing elements in List
res = list(set(range(max(test_list) + 1)) - set(test_list))

# print result
print("The list of missing elements : " + str(res))
