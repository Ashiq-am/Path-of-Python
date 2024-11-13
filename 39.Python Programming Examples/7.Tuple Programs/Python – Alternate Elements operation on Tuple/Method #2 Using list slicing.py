# Python3 code to demonstrate working of
# Alternate Elements operation on Tuple
# Using list slicing

# initializing tuple
test_tuple = (5, 6, 3, 6, 10, 34)

# printing original tuple
print("The original tuple : " + str(test_tuple))

# Alternate Elements operation on Tuple
# Using list slicing
sum1 = sum(test_tuple[1::2])
sum2 = sum(test_tuple[0::2])

# printing result
print("The alternate chain sum 1 : " + str(sum1))
print("The alternate chain sum 2 : " + str(sum2))
