# Python program to illustrate the
# conversion of a byte string
# to a list of integers

# Initializing a byte string
byte_val = b'\xfc\x00'

# 2's complement is enabled in big
# endian byte order format
int_val = int.from_bytes(byte_val, "big", signed="True")

# Printing int object
print(int_val)
