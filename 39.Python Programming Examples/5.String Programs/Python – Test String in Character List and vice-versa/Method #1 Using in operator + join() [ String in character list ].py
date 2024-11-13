# Python3 code to demonstrate working of
# Test String in Character List and vice-versa
# Using in operator and join() [String in list]

# initializing string
test_str = 'geeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing Character list
K = ['g', 'e', 'e', 'k', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's']

# joining list
joined_list = ''.join(K)

# checking for presence
res = test_str in joined_list

# printing result
print("Is String present in character list : " + str(res))
