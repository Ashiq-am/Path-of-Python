# Python3 code to demonstrate working of
# Split URL from Query Parameters
# Using split()

# initializing string
test_str = 'www.geeksforgeeks.org?is = best'

# printing original string
print("The original string is : " + str(test_str))

# Split URL from Query Parameters
# Using split()
res = test_str.split('?')[0]

# printing result
print("The base URL is : " + res)
