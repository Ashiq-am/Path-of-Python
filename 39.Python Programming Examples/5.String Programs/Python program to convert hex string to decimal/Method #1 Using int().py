# Python3 code to demonstrate
# converting hexadecimal string to decimal
# Using int()

# initializing string
test_string = 'A'

# printing original string
print("The original string : " + str(test_string))

# using int()
# converting hexadecimal string to decimal
res = int(test_string, 16)

# print result
print("The decimal number of hexadecimal string : " + str(res))
