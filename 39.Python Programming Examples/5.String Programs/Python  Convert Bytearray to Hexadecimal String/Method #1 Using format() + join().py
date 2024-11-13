# Python3 code to demonstrate working of
# Converting bytearray to hexadecimal string
# Using join() + format()

# initializing list
test_list = [124, 67, 45, 11]

# printing original list
print("The original string is : " + str(test_list))

# using join() + format()
# Converting bytearray to hexadecimal string
res = ''.join(format(x, '02x') for x in test_list)

# printing result
print("The string after conversion : " + str(res))
