'''The int type implements the numbers.Integral abstract base class.'''




num = 7
print(num.bit_length())

num = -7
print(num.bit_length())




'''1. int.bit_length()
Returns the number of bits required to represent an integer in binary, excluding the sign and leading zeros.

Code to demonstrate'''







# Returns byte representation of 1024 in a
# big endian machine.
print((1024).to_bytes(2, byteorder ='big'))




'''2. int.to_bytes(length, byteorder, *, signed=False)
Return an array of bytes representing an integer.'''






# Returns integer value of '\x00\x10' in big endian machine.
print(int.from_bytes(b'\x00\x10', byteorder ='big'))




'''3. int.from_bytes(bytes, byteorder, *, signed=False)
Returns the integer represented by the given array of bytes.'''
