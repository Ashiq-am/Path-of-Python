# Python3 code to demonstrate working of
# Subscript Dictionary
# Using loop + ord()

# initializing string
test_str = "0123456789"

# printing original string
print("The original string is : " + test_str)

# initializing Subscript number value
K = u'\u2080'

# Subscript Dictionary
# Using loop + ord()
res = {}
for ele in test_str:
	res[ele] = K
	K = chr(ord(K) + 1)

# printing result
print("The split string is : " + str(res))
