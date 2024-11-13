# Python3 code to demonstrate working of
# Test if String contains any Uppercase character
# Using any() + isupper()

# initializing string
test_str = 'geeksforGeeks'

# printing original string
print("The original string is : " + str(test_str))

# Using any() to check for any element to be uppercase
res = any(ele.isupper() for ele in test_str)

# printing result
print("Does String contain uppercase character : " + str(res))
