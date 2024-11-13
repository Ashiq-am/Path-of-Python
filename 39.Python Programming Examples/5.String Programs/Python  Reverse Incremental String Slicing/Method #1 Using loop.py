# Python3 code to demonstrate working of
# Reverse Incremental String Slicing
# Using loop

# initializing string
test_str = "geeks"

# printing original string
print("The original string is : " + test_str)

# Reverse Incremental String Slicing
# Using loop
res = []
sub = ''
for chr in reversed(test_str):
	sub += chr
	res.append(sub)

# printing result
print("The incremental reverse strings : " + str(res))
