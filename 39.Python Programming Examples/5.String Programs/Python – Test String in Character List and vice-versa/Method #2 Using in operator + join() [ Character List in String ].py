# Python3 code to demonstrate working of
# Test String in Character List and vice-versa
# Using in operator + join() [ Character List in String ]

# initializing string
test_str = 'geeksforgeeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing Character list
K = ['g', 'e', 'e', 'k', 's']

# joining list
joined_list = ''.join(K)

# checking for presence
res = joined_list in test_str

# printing result
print("Is character list present in String : " + str(res))
