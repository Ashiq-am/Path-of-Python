# Python3 code to demonstrate working of
# Convert location coordinates to tuple
# Using tuple() + float() + split() + map()

# Initializing string
test_str = "44.6463, -49.583"

# printing original string
print("The original string is : " + str(test_str))

# Convert location coordinates to tuple
# Using tuple() + float() + split() + map()
res = tuple(map(float, test_str.split(', ')))

# printing result
print("The coordinates after conversion to tuple are : " + str(res))
