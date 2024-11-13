# Python3 code to demonstrate working of
# Convert location coordinates to tuple
# Using eval()

# Initializing string
test_str = "44.6463, -49.583"

# printing original string
print("The original string is : " + str(test_str))

# Convert location coordinates to tuple
# Using eval()
res = eval(test_str)

# printing result
print("The coordinates after conversion to tuple are : " + str(res))
