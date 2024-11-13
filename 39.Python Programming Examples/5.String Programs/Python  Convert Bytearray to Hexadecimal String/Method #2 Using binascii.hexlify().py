# Python3 code to demonstrate working of
# Converting bytearray to hexadecimal string
# Using binascii.hexlify()
import binascii

# initializing list
test_list = [124, 67, 45, 11]

# printing original list
print("The original string is : " + str(test_list))

# using binascii.hexlify()
# Converting bytearray to hexadecimal string
res = binascii.hexlify(bytearray(test_list))

# printing result
print("The string after conversion : " + str(res))
