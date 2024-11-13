# Python3 code to demonstrate
# splitting string to list of characters.
# using list slicing

# initializing string
test_string = "GeeksforGeeks"

# printing original string
print ("The original string is : " + str(test_string))

# using list slicing
# for splitting string to list of characters
res = []
res[:] = test_string

# printing result
print ("The resultant list of characters : " + str(res))
