# Python3 code to demonstrate
# Extract digit string
# using join() + isdigit() + filter()

# initializing string
test_string = 'g1eeks4geeks5'

# printing original strings
print("The original string : " + test_string)

# using join() + isdigit() + filter()
# Extract digit string
res = ''.join(filter(lambda i: i.isdigit(), test_string))

# print result
print("The digits string is : " + str(res))
