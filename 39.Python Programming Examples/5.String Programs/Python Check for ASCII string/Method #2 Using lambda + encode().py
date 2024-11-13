# Python3 code to demonstrate
# Check for ASCII string
# using lambda + encode()

# initializing string
test_string = "G4G is best"

# printing original string
print("The original string : " + str(test_string))

# using lambda + encode()
# Check for ASCII string
res = lambda ele: len(ele) == len(ele.encode())

# print result
print("Is the string full ASCII ? : " + str(res(test_string)))
