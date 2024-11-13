# Python3 code to demonstrate working of
# Replace occurrences by K except first character
# Using replace()

# initializing string
test_str = 'geeksforgeeksforgeeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = '$'

# replacing using replace()
res = test_str.replace(test_str[0], K).replace(K, test_str[0], 1)

# printing result
print("Replaced String : " + str(res))
