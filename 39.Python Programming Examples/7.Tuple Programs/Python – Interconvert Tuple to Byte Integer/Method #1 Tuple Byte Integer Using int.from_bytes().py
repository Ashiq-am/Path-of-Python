# Python3 code to demonstrate working of
# Interconvert Tuple to Byte Integer
# Tuple -> Byte Integer : Using int.from_bytes()

# initializing tuples
test_tuple = (6, 8, 3, 2)

# printing original tuple
print("The original tuple : " + str(test_tuple))

# Interconvert Tuple to Byte Integer
# Tuple -> Byte Integer : Using int.from_bytes()
res = int.from_bytes(test_tuple, byteorder ='big')

# printing result
print("Tuple after conversion : " + str(res))
