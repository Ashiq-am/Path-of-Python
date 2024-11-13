# Python3 code to demonstrate
# Add leading K character
# using format()

# initializing string
test_string = 'GFG'

# printing original string
print("The original string : " + str(test_string))

# No. of zeros required
N = 4

# initializing K
K = '0'

# using format()
# Add leading K character
# N for number of elememts and '>' for leading
temp = '{:>' + K + '7}'
res = temp.format(test_string)

# print result
print("The string after adding leading K : " + str(res))
