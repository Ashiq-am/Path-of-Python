# Python3 code to demonstrate working of
# Test if String contains any Uppercase character
# Using isupper() + loop

# initializing string
test_str = 'geeksforGeeks'

# printing original string
print("The original string is : " + str(test_str))

res = False
for ele in test_str:

	# checking for uppercase character and flagging
	if ele.isupper():
		res = True
		break

# printing result
print("Does String contain uppercase character : " + str(res))
