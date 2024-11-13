# Python3 code to demonstrate working of
# Test if String contains any Uppercase character
# Using any() + ASCII values

# initializing string
test_str = 'geeksforGeeks'

# printing original string
print("The original string is : " + str(test_str))

# Using ascii values check for any element to be uppercase
res = any(ord(ele) != 32 and ord(ele) <=
		64 or ord(ele) >= 91 for ele in test_str)

# printing result
print("Does String contain uppercase character : " + str(res))
