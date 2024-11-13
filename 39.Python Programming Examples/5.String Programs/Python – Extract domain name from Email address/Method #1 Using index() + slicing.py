# Python3 code to demonstrate working of
# Extract domain name from Email address
# Using index() + slicing

# initializing strings
test_str = 'manjeet@geeksforgeeks.com'

# printing original string
print("The original string is : " + str(test_str))

# slicing domain name using slicing
res = test_str[test_str.index('@') + 1 : ]

# printing result
print("The extracted domain name : " + str(res))
