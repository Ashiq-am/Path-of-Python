# Python3 code to demonstrate
# Get first index values in tuple of strings
# using next() + zip()

# initializing tuple
test_tuple = ('GfG', 'for', 'Geeks')

# printing original tuple
print("The original tuple : " + str(test_tuple))

# using next() + zip()
# Get first index values in tuple of strings
res = list(next(zip(*test_tuple)))

# print result
print("The first index string character list : " + str(res))
