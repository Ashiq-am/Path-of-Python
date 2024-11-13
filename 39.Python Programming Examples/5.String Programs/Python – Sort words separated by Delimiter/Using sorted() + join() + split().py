# Python3 code to demonstrate working of
# Sort words seperated by Delimiter
# Using split() + join() + sorted()

# initializing string
test_str = 'gfg:is:best:for:geeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing Delimiter
delim = ":"

# joining the sorted string after split
res = delim.join(sorted(test_str.split(':')))

# printing result
print("The sorted words : " + str(res))
