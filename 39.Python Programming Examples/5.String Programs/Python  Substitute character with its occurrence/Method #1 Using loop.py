# Python3 code to demonstrate working of
# Substitute character with its occurrence
# Using loop

# initializing string
test_str = "geeksforgeeks is best for geeks"

# printing original string
print("The original string is : " + test_str)

# initializing letter
test_let = 'g'

# Substitute character with its occurrence
# Using loop
res = ''
count = 1
for chr in test_str:
	if chr == test_let:
		res += str(count)
		count += 1
	else:
		res += chr

# printing result
print("The string after performing substitution : " + str(res))
