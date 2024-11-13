# Python code to demonstrate
# to find common prefix
# from set of strings

# Initialising string
ini_strlist = ['akshat', 'akash', 'akshay', 'akshita']

# Finding commom prefix using Naive Approach
res = ''
prefix = ini_strlist[0]

for string in ini_strlist[1:]:
	while string[:len(prefix)] != prefix and prefix:
		prefix = prefix[:len(prefix)-1]
	if not prefix:
		break
res = prefix

# Printing result
print("Resultant prefix", str(res))
