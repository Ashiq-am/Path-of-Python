# Python3 code to demonstrate working of
# Filter Supersequence Strings
# Using filter() + all()

# initializing list
test_list = ["gfg", "/", "geeksforgeeks", "best", "for", "geeks"]

# printing original list
print("The original list is : " + str(test_list))

# initializing substr
substr = "kgs"

# all() checks for all characters in strings
res = list(filter(lambda sub: all(ele in sub for ele in substr), test_list))

# printing result
print("Filtered strings : " + str(res))
