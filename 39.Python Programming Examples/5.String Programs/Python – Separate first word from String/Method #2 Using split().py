# Python3 code to demonstrate working of
# Separate first word from String
# Using split()

# initializing string
test_str = "gfg is best"

# printing original string
print("The original string is : " + test_str)

# Separate first word from String
# Using split()
res = test_str.split(' ', 1)

# printing result
print("Initial word separated list : " + str(res))
