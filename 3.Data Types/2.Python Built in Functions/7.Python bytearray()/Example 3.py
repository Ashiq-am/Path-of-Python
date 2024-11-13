# Creates bytearray from byte literal
arr1 = bytearray(b"abcd")

# iterating the value
for value in arr1:
    print(value)

# Create a bytearray object
arr2 = bytearray(b"aaaacccc")

# count bytes from the buffer
print("Count of c is:", arr2.count(b"c"))
