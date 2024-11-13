# Python3 code to demonstrate working of
# Subscript Dictionary
# Using Dictionary comprehension

# initializing string
test_str = "0123456789"

# printing original string
print("The original string is : " + test_str)

# initializing Subscript number value
K = u'\u2080'

# Subscript Dictionary
# Using Dictionary comprehension
res = {ele : chr(ord(K) + 1) for ele in test_str}

# printing result
print("The split string is : " + str(res))
