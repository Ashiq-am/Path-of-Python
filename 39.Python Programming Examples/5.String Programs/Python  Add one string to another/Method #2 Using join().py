# Python code to demonstrate
# Adding one string to another
# Using join()

# initializing string
test_string = "GFG"

# initializing add_string
add_string = " is best"

# printing original string
print("The original string : " + str(test_string))

# printing original add string
print("The add string : " + str(add_string))

# Using join()
# adding one string to another
res = "".join((test_string, add_string))

# print result
print("The concatenated string is : " + res)
