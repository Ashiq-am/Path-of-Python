# Python3 code to demonstrate working of
# Inserting a number in string
# Using % d operator

# initializing string
test_str = "Geeks"

# initializing number
test_int = 4

# printing original string
print("The original string is : " + test_str)

# printing number
print("The original number : " + str(test_int))

# using % d operator
# Inserting number in string
res = (test_str + "% d" + test_str) % test_int

# printing result
print("The string after adding number is : " + str(res))
