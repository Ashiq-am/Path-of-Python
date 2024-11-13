# Python3 code to demonstrate working of
# N sized substrings with K distinct characters
# Using slicing + set() + loop

# initializing string
test_str = 'geeksforgeeksforgeeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing N
N = 3

# initializing K
K = 2

res = []
for idx in range(0, len(test_str) - N + 1):

	# getting unique elements off sliced string
	if (len(set(test_str[idx: idx + N])) == K):
		res.append(test_str[idx: idx + N])

# printing result
print("Extracted Strings : " + str(res))
