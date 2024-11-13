# Python3 code to demonstrate working of
# Prefix extraction before specific character
# Using rsplit()

# initializing string
test_str = "GeeksforGeeks"

# initializing split character
spl_char = "r"

# printing original string
print("The original string is : " + str(test_str))

# Using rsplit()
# Prefix extraction before specific character
res = test_str.rsplit(spl_char, 1)[0]

# printing result
print("The prefix string is : " + str(res))
