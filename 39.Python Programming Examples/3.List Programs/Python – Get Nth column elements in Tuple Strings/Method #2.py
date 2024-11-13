# Python3 code to demonstrate
# Nth column in Tuple Strings
# using next() + zip()

# initializing tuple
test_tuple = ('GfG', 'for', 'Geeks')

# printing original tuple
print("The original tuple : " + str(test_tuple))

# initializing N
N = 1

# using next() + zip()
# Nth column in Tuple Strings
temp = zip(*test_tuple)
for idx in range(0, N):
	next(temp)
res = list(next(temp))

# print result
print("The Nth index string character list : " + str(res))
