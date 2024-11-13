# Python3 code to demonstrate working of
# Extract suffix after K
# Using rpartition()

# initializing string
test_str = "GeeksforGeeks"

# initializing split character
spl_char = "r"

# printing original string
print("The original string is : " + str(test_str))

# Using rpartition()
# Extract suffix after K
res = test_str.rpartition(spl_char)[2]

# printing result
print("The suffix string is : " + str(res))
