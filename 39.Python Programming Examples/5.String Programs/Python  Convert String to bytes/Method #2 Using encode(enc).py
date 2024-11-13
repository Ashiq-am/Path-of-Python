# Python code to demonstrate
# convert string to byte
# Using encode(enc)

# initializing string
test_string = "GFG is best"

# printing original string
print("The original string : " + str(test_string))

# Using encode(enc)
# convert string to byte
res = test_string.encode('utf-8')

# print result
print("The byte converted string is : " + str(res) + ", type : " + str(type(res)))
