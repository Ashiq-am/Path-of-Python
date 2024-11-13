# Python program to demonstrate
# RIPEMD


import hashlib

# Passing the required algorithm
# as string to the new constructor
x = hashlib.new('ripemd160')

# passing GeeksforGeeks
# to x() which uses
# ripemd 160 algorithm for
# hashing
x.update(b"GeeksForGeeks")

# printing the equivalent hexadecimal
# value.
print("The byte equivalent of hash is :")
print(x.digest())
