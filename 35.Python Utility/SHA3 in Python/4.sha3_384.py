# import the library module
import sys
import hashlib

if sys.version_info < (3, 6):
	import sha3

# initialize a string
str = "GeeksforGeeks"

# encode the string
encoded_str = str.encode()

# create sha3-384 hash objects
obj_sha3_384 = hashlib.sha3_384(encoded_str)

# print in hexadecimal
print("\nSHA3-384 Hash: ", obj_sha3_384.hexdigest())
