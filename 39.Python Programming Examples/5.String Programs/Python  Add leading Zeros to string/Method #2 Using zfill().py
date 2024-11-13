# Python3 code to demonstrate
# adding leading zeros
# using zfill()

# initializing string
test_string = 'GFG'

# printing original string
print("The original string : " + str(test_string))

# No. of zeros required
N = 4

# using zfill()
# adding leading zero
res = test_string.zfill(N + len(test_string))

# print result
print("The string after adding leading zeros : " + str(res))
