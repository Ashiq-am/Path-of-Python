# Python3 code to demonstrate working of
# Custom Consecutive Character Pairing
# Using windowed() + loop
import more_itertools

# initializing string
test_str = 'geeksforgeeks'

# printing original string
print("The original string is : " + test_str)

# initializing Delim
delim = '_'

# Custom Consecutive Character Pairing
# Using windowed() + loop
res = []
for ele in more_itertools.windowed(test_str, 2):
	res.append(ele[0] + delim + ele[1])

# printing result
print("The List of joined Characters : " + str(res))
