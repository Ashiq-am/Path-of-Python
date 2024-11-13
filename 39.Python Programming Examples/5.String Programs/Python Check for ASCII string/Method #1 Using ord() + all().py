# Python3 code to demonstrate
# Check for ASCII string
# using all() + ord()

# initializing string
test_string = "G4G is best"

# printing original string
print("The original string : " + str(test_string))

# using all() + ord()
# Check for ASCII string
res = all(ord(c) < 128 for c in test_string)

# print result
print("Is the string full ASCII ? : " + str(res))
