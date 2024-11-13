# Python3 code to demonstrate working of
# Extract range characters from String
# Using filter() + lambda + join()

# initializing string
test_str = 'geekforgeeks is best'

# printing original string
print("The original string is : " + str(test_str))

# initializing range letters
strt, end = "f", "s"

# join() to get result in string
res = ''.join(list(filter(lambda chr : chr >= strt and chr <= end, test_str)))

# printing result
print("Extracted String : " + str(res))
