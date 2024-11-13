# Python3 code to demonstrate working of
# Remove all consonents from string
# Using loop

# initializing string
test_str = "Gfg is best for geeks"

# printing original string
print("The original string is : " + test_str)

# Remove all consonents from string
# Using loop
res = []
for chr in test_str:
	if chr in "aeiouAEIOU":
		res.extend(chr)
res = "".join(res)

# printing result
print("String after consonents removal : " + str(res))
