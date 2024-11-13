# Python3 code to demonstrate working of
# Word starting at Index
# Using split() + list slicing

# initializing string
test_str = "gfg is best for geeks"

# printing original string
print("The original string is : " + test_str)

# initializing K
K = 7

# Word starting at Index
# Using split() + list slicing
res = test_str[K:].split()[0]

# printing result
print("Word at index K : " + str(res))
