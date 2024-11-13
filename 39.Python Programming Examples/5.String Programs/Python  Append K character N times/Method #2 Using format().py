# Python3 code to demonstrate
# Append K character N times
# using format()

# initializing string
test_string = 'GFG'

# printing original string
print("The original string : " + str(test_string))

# initializing K
K = '0'

# No. of zeros required
N = 5

# using format()
# Append K character N times
temp = '{:<' + K + str(len(test_string) + N) + '}'
res = temp.format(test_string)

# print result
print("The string after adding trailing K : " + str(res))
