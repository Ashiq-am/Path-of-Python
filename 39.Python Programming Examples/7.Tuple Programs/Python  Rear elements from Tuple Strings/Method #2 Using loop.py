# Python3 code to demonstrate
# Rear elements from Tuple Strings
# using list comprehension

# initializing tuple
test_tuple = ('GfG', 'for', 'Geeks')

# printing original tuple
print("The original tuple : " + str(test_tuple))

# using list comprehsion
# Rear elements from Tuple Strings
res = []
for sub in test_tuple :
	N = len(sub) - 1
	res.append(sub[N])

# print result
print("The rear index string character list : " + str(res))
