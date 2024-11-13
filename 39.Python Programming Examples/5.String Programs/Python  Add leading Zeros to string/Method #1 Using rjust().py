# Python3 code to demonstrate
# adding leading zeros
# using rjust()

# initializing string
test_string = 'GFG'

# printing original string
print("The original string : " + str(test_string))

# No. of zeros required
N = 4

# using rjust()
# adding leading zero
res = test_string.rjust(N + len(test_string), '0')

# print result
print("The string after adding leading zeros : " + str(res))
