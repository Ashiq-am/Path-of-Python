# Python program to illustrate the
# conversion of a byte string
# to a list of integers

# Initializing byte value
byte_val = b'\x00\x01'

# Converting to int
# byteorder is big where MSB is at start
int_val = int.from_bytes(byte_val, "big")

# Printing int equivalent
print(int_val)
