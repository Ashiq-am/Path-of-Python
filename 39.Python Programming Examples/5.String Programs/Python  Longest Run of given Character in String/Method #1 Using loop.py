# Python3 code to demonstrate working of
# Longest Run of Character in String
# Using loop

# initializing string
test_str = 'geeksforgeeeks'

# printing original string
print("The original string is : " + test_str)

# initializing K
K = 'e'

# Longest Run of Character in String
# Using loop
res = 0
cnt = 0
for chr in test_str:
	if chr == K:
		cnt += 1
	else:
		res = max(res, cnt)
		cnt = 0
res = max(res, cnt)

# printing result
print("Longest Run length of K : " + str(res))
