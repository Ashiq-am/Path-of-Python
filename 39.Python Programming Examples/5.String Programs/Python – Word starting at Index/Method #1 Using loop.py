# Python3 code to demonstrate working of
# Word starting at Index
# Using loop

# initializing string
test_str = "gfg is best for geeks"

# printing original string
print("The original string is : " + test_str)

# initializing K
K = 7

# Word starting at Index
# Using loop
res = ''
for idx in range(K, len(test_str)):
	if test_str[idx] == ' ':
		break
	res += test_str[idx]

# printing result
print("Word at index K : " + str(res))
