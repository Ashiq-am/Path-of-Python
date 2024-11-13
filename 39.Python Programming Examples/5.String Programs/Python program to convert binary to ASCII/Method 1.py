# Python program to illustrate the
# conversion of Binary to ASCII

# Importing binascii module
import binascii

# Initializing a binary string
Text = b"GFG is a CS Portal"

# Calling the b2a_uu() function to
# Convert the binary string to ascii
Ascii = binascii.b2a_uu(Text)

# Getting the ASCII equivalent
print(Ascii)
