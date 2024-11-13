# Python3 code to demonstrate working of
# Longest Consecution without K in String
# Using loop

# initializing string
test_str = 'geeksforgeeks is best for geeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = 'e'

# getting all indices
indxs = []
for idx, ele in enumerate(test_str):
	if ele == 'e':
		indxs.append(idx)

# getting difference
diffs = []
for idx in range(len(indxs) - 1):
	diffs.append(indxs[idx + 1] - indxs[idx])

# getting max diff using max()
res = max(diffs)

# printing result
print("Longest run : " + str(res))
