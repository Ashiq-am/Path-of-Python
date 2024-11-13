# Python3 code to demonstrate
# getting size of string in bytes
# using encode() + len()

# initializing string
test_string = "geekforgeeks"

# printing original string
print("The original string : " + str(test_string))

# using encode() + len()
# getting size of string in bytes
res = len(test_string.encode('utf-8'))

# print result
print("The length of string in bytes : " + str(res))
