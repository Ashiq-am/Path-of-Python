# Python3 code to demonstrate working of
# Split URL from Query Parameters
# Using rfind()

# initializing string
test_str = 'www.geeksforgeeks.org?is = best'

# printing original string
print("The original string is : " + str(test_str))

# Split URL from Query Parameters
# Using rfind()
res = test_str[:test_str.rfind('?')]

# printing result
print("The base URL is : " + res)
