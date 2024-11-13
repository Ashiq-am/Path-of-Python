# Python3 code to demonstrate working of
# Alternate character addition
# Using loop

# initializing string
test_str = "geeksforgeeks"

# printing original string
print("The original string is : " + test_str)

# initializing K
K = '*'

# Alternate character addition
# Using loop
res = ''
for ele in test_str:
	res += ele + K
res = res[:-1]

# printing result
print("String after character addition : " + str(res))
