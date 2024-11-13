# Python3 code to demonstrate working of
# Replace all words not K
# Using list comprehension

# initializing string
test_str = 'gfg is best for geeks gfg is for cs I love gfg'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = "gfg"

# initializing repl_char
repl_char = "?"

# using one-liner to solve this problem
res = " ".join(
	[repl_char if not ele == K else ele for ele in test_str.split()])

# printing result
print("The resultant string : " + str(res))
