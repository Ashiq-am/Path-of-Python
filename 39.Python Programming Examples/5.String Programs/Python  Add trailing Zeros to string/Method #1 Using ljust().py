# Python3 code to demonstrate
# adding trailing zeros
# using ljust()

# initializing string
test_string = 'GFG'

# printing original string
print("The original string : " + str(test_string))

# No. of zeros required
N = 4

# using ljust()
# adding trailing zero
res = test_string.ljust(N + len(test_string), '0')

# print result
print("The string after adding trailing zeros : " + str(res))
