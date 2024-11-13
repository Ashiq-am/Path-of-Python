# Python3 code to demonstrate working of
# Interconvert Tuple to Byte Integer
# Using Byte Integer -> Tuple : Using tuple.to_bytes()

# initializing integer
test_int = 101188354

# printing original integer
print("The original integer : " + str(test_int))

# Interconvert Tuple to Byte Integer
# Using Byte Integer -> Tuple : Using tuple.to_bytes()
res = tuple(test_int.to_bytes(4, byteorder ='big'))

# printing result
print("Integer after conversion : " + str(res))
