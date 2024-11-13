# Python3 code to demonstrate working of
# Extract String till all occurrence of characters from other string
# Using find() + max() + slice

# initializing string
test_str = "geeksforgeeks is best for all geeks"

# printing original string
print("The original string is : " + str(test_str))

# initializing check string
check_str = "freak"

# max() find maximum index of all characters
res = test_str[:max([test_str.find(idx) for idx in check_str]) + 1]

# printing result
print("String till all characters occurred : " + str(res))
