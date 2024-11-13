# Python3 code to demonstrate working of
# Alternate Elements operation on Tuple
# Using loop + enumerate()

# initializing tuple
test_tuple = (5, 6, 3, 6, 10, 34)

# printing original tuple
print("The original tuple : " + str(test_tuple))

# Alternate Elements operation on Tuple
# Using loop + enumerate()
sum1 = 0
sum2 = 0
for idx, ele in enumerate(test_tuple):
	if idx % 2:
		sum1 += ele
	else :
		sum2 += ele

# printing result
print("The alternate chain sum 1 : " + str(sum1))
print("The alternate chain sum 2 : " + str(sum2))
