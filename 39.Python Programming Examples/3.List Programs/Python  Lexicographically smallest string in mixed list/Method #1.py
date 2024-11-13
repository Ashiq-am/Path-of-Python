# Python3 code to demonstrate working of
# Lexicographically smallest string in mixed list
# Using min() + isinstance() + list comprehension

# initializing list
test_list = [1, 2, 4, "GFG", 5, "IS", 7, "BEST"]

# printing original list
print("The original list is : " + str(test_list))

# Lexicographically smallest string in mixed list
# Using min() + isinstance() + list comprehension
res = min(sub for sub in test_list if isinstance(sub, str))

# printing result
print("The Lexicographically smallest string is : " + str(res))
