# Python3 code to demonstrate
# Add leading K character
# using rjust()

# initializing string
test_string = 'GFG'

# printing original string
print("The original string : " + str(test_string))

# No. of zeros required
N = 4

# initializing K
K = 'M'

# using rjust()
# Add leading K character
res = test_string.rjust(N + len(test_string), K)

# print result
print("The string after adding leading K : " + str(res))
