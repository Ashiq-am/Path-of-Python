# Python3 code to demonstrate working of
# Extract Upper Case Characters
# Using filter() + lambda

# initializing string
test_str = "GeeksForGeeKs"

# printing original string
print("The original string is : " + str(test_str))

# Extract Upper Case Characters
# Using filter() + lambda
res = list(filter(lambda c: c.isupper(), test_str))

# printing result
print("The uppercase characters in string are : " + str(res))
