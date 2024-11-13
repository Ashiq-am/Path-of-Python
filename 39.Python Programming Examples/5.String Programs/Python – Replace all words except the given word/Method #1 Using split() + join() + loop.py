# Python3 code to demonstrate working of
# Replace all words not K
# Using join() + split() + loop

# initializing string
test_str = 'gfg is best for geeks gfg is for cs I love gfg'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = "gfg"

# initializing repl_char
repl_char = "?"

# extracting words
temp = test_str.split(" ")
for idx in range(len(temp)):
	ele = temp[idx]

	# replace non K with repl_char
	if not ele == K:
		temp[idx] = repl_char

# joining result
res = " ".join(temp)

# printing result
print("The resultant string : " + str(res))
