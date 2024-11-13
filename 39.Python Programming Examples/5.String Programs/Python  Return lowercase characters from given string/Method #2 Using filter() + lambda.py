# Python3 code to demonstrate working of
# Return lowercase characters in string
# Using filter() + lambda

# initializing string
test_str = "GeeksForGeeKs"

# printing original string
print("The original string is : " + str(test_str))

# Return lowercase characters in string
# Using filter() + lambda
res = list(filter(lambda c: c.islower(), test_str))

# printing result
print("The lowercase characters in string are : " + str(res))
