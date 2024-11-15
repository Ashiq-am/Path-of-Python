# Python program to illustrate the
# conversion of ASCII to Binary

# Calling string.encode() function to
# turn the specified string into an array
# of bytes
byte_array = "GFG".encode()

# Converting the byte_array into a binary
# integer
binary_int = int.from_bytes(byte_array, "big")

# Converting binary_int to a string of
# binary characters
binary_string = bin(binary_int)

# Getting the converted binary characters
print(binary_string)
