# Python program to illustrate the
# conversion of ASCII to Binary

# Importing binascii module
import binascii

# Initializing a ASCII string
Text = "21T9'(&ES(&$@0U,@4&]R=&%L"

# Calling the a2b_uu() function to
# Convert the ascii string to binary
Binary = binascii.a2b_uu(Text)

# Getting the Binary value
print(Binary)
