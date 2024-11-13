# Python3 code to demonstrate working of
# N sized substrings with K distinct characters
# Using list comprehension + len() + set() + slicing

# initializing string
test_str = 'geeksforgeeksforgeeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing N
N = 3

# initializing K
K = 2

# list comprehension used to slice
res = [test_str[idx: idx + N]
	for idx in range(0, len(test_str) - N + 1)
	if len(set(test_str[idx: idx + N])) == K]

# printing result
print("Extracted Strings : " + str(res))
