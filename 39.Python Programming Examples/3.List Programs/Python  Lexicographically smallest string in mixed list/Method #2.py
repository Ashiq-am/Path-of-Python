# Python3 code to demonstrate working of
# Lexicographically smallest string in mixed list
# Using min() + lambda + filter()

# initializing list
test_list = [1, 2, 4, "GFG", 5, "IS", 7, "BEST"]

# printing original list
print("The original list is : " + str(test_list))

# Lexicographically smallest string in mixed list
# Using min() + lambda + filter()
res = min(filter(lambda s:isinstance(s, str), test_list))

# printing result
print("The Lexicographically smallest string is : " + str(res))
