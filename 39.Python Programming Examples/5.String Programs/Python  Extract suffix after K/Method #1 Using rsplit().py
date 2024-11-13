# Python3 code to demonstrate working of
# Extract suffix after K
# Using rsplit()

# initializing string
test_str = "GeeksforGeeks"

# initializing split character
spl_char = "r"

# printing original string
print("The original string is : " + str(test_str))

# Using rsplit()
# Extract suffix after K
res = test_str.rsplit(spl_char, 1)[1]

# printing result
print("The suffix string is : " + str(res))
