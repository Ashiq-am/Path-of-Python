# Python3 code to demonstrate working of
# Rear stray character String split
# Using split() + rstrip()

# initializing string
test_str = 'gfg, is, best, '

# printing original string
print("The original string is : " + test_str)

# Rear stray character String split
# Using split() + rstrip()
res = test_str.rstrip(', ').split(', ')

# printing result
print("The evaluated result is : " + str(res))
