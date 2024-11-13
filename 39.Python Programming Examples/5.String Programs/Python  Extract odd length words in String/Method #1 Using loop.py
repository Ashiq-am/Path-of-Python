# Python3 code to demonstrate working of
# Extract odd length words in String
# Using loop

# initializing string
test_str = "gfg is best of geeks"

# printing original string
print("The original string is : " + test_str)

# Extract odd length words in String
# Using loop
res = []
for ele in test_str.split():
	if len(ele) % 2 :
		res.append(ele)

# printing result
print("The odd length strings are : " + str(res))
