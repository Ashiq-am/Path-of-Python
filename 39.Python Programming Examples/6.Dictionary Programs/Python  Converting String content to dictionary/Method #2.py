# Python3 code to demonstrate working of
# Converting String content to dictionary
# Using eval()

# initializing string
test_str = "Gfg = 1, Good = 2, CS = 3, Portal = 4"

# printing original string
print("The original string is : " + test_str)

# Using eval()
# Converting String content to dictionary
res = eval('dict(% s)' % test_str)

# printing result
print("The newly created dictionary : " + str(res))
