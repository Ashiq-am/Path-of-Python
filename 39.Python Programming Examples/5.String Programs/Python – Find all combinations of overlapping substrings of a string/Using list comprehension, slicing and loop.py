# Python3 code to demonstrate working of
# Overlapping substrings of all lengths
# Using list comprehension + slicing + loop

# initializing string
test_str = 'Geeks4G'

# printing original string
print("The original string is : " + str(test_str))

# manipulating overlap size using loop
res = []
for idx in range(len(test_str) + 1):

	# getting overlap strings
	res.append([test_str[j: j + idx] for j in range(len(test_str) - idx + 1)])

# printing result
print("All overlapping Strings : " + str(res))
