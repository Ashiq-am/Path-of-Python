# Python3 code to demonstrate working of
# Extract domain name from Email address
# Using split()

# initializing strings
test_str = 'manjeet@geeksforgeeks.com'

# printing original string
print("The original string is : " + str(test_str))

# using split() to get domain name
res = test_str.split('@')[1]

# printing result
print("The extracted domain name : " + str(res))
