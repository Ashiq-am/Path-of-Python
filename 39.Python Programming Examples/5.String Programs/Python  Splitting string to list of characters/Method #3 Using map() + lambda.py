# Python3 code to demonstrate
# splitting string to list of characters.
# using map() + lambda

# initializing string
test_string = "GeeksforGeeks"

# printing original string
print ("The original string is : " + str(test_string))

# using map() + lambda
# for splitting string to list of characters
res = list(map(lambda i:i, test_string))

# printing result
print ("The resultant list of characters : " + str(res))
