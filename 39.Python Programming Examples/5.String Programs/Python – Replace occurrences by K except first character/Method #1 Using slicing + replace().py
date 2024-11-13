# Python3 code to demonstrate working of
# Replace occurrences by K except first character
# Using slicing + replace()

# initializing string
test_str = 'geeksforgeeksforgeeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = '$'

# replacing using replace()
res = test_str[0] + test_str[1:].replace(test_str[0], K)

# printing result
print("Replaced String : " + str(res))
