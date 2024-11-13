# Python code to demonstrate
# convert string to byte
# Using bytes(str, enc)

# initializing string
test_string = "GFG is best"

# printing original string
print("The original string : " + str(test_string))

# Using bytes(str, enc)
# convert string to byte
res = bytes(test_string, 'utf-8')

# print result
print("The byte converted string is : " + str(res) + ", type : " + str(type(res)))
