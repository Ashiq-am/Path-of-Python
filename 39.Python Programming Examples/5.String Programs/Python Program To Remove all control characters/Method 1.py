# Python3 code to demonstrate working of
# Remove all control characters
# Using translate()

# initializing string
test_str = 'Geeks\0\r for \n\bge\tee\0ks\f'

# printing original string
print("The original string is : " + str(test_str))

# using translate() and fromkeys()
# to escape all control characters
mapping = dict.fromkeys(range(32))
res = test_str.translate(mapping)

# printing result
print("String after removal of control characters : " + str(res))
