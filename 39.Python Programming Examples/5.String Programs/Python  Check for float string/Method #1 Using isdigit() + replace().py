# Python3 code to demonstrate
# Check for float string
# using isdigit() + replace()

# initializing string
test_string = "45.657"

# printing original string
print("The original string : " + str(test_string))

# using isdigit() + replace()
# Check for float string
res = test_string.replace('.', '', 1).isdigit()

# print result
print("Is string a possible float number ? : " + str(res))
