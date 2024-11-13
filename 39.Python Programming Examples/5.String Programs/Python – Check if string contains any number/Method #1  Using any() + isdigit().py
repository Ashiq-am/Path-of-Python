# Python3 code to demonstrate working of
# Check if string contains any number
# Using isdigit() + any()

# initializing string
test_str = 'geeks4geeks'

# printing original string
print("The original string is : " + str(test_str))

# using any() to check for any occurrence
res = any(chr.isdigit() for chr in test_str)

# printing result
print("Does string contain any digit ? : " + str(res))
