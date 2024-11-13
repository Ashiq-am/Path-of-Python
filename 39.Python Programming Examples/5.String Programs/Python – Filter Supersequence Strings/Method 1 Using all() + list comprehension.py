# Python3 code to demonstrate working of
# Filter Supersequence Strings
# Using all() + list comprehension

# initializing list
test_list = ["gfg", "/", "geeksforgeeks", "best", "for", "geeks"]

# printing original list
print("The original list is : " + str(test_list))

# initializing substr
substr = "kgs"

# all() checks for all characters in strings
res = [sub for sub in test_list if all(ele in sub for ele in substr)]

# printing result
print("Filtered strings : " + str(res))
