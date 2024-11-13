# Python3 code to demonstrate working of
# Extract range characters from String
# Using list comprehension

# initializing string
test_str = 'geekforgeeks is best'

# printing original string
print("The original string is : " + str(test_str))

# initializing range letters
strt, end = "f", "s"

# join() to get result in string
res = ''.join([chr for chr in test_str if chr >= strt and chr <= end])

# printing result
print("Extracted String : " + str(res))
