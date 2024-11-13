# Python3 code to demonstrate working of
# Inserting a number in string
# Using type conversion

# initializing string
test_str = "Geeks"

# initializing number
test_int = 4

# printing original string
print("The original string is : " + test_str)

# printing number
print("The original number : " + str(test_int))

# using type conversion
# Inserting number in string
res = test_str + str(test_int) + test_str

# printing result
print("The string after adding number is : " + str(res))
