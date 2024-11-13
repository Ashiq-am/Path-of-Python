# Python3 code to demonstrate working of
# Count K character between consecutive characters
# Using loop

# initializing string
test_str = "g...f..g.i..s....b..e....s...t"

# printing original string
print("The original string is : " + test_str)

# initializing K
K = '.'

# Count K character between consecutive characters
# Using loop
count = 0
res = []
for ele in test_str:
	if ele == K:
		count += 1
	else:
		res.append(count)
		count = 0
res = res[1:]

# printing result
print("List of character count : " + str(res))
