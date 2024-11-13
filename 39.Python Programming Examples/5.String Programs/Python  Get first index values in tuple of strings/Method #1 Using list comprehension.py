# Python3 code to demonstrate
# Get first index values in tuple of strings
# using list comprehension

# initializing tuple
test_tuple = ('GfG', 'for', 'Geeks')

# printing original tuple
print("The original tuple : " + str(test_tuple))

# using list comprehsion
# Get first index values in tuple of strings
res = list(sub[0] for sub in test_tuple)

# print result
print("The first index string character list : " + str(res))
