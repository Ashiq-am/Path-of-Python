# Python3 code to demonstrate working of
# Remove digits before K Number
# Using split() + enumerate() + index() + list comprehension

# initializing string
test_str = 'geeksforgeeks 2 6 is 4 geeks 5 and CS8'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = 4

# get K Number index
idx = test_str.split().index(str(K))

# isdigit() used to check for number
res = [ele for i, ele in enumerate(test_str.split()) if not (i < idx and ele.isdigit())]
res = ' '.join(res)


# printing result
print("String after removing digits before K : " + str(res))
