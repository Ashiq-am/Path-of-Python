# Python3 code to demonstrate
# Rear elements from Tuple Strings
# using list comprehension

# initializing tuple
test_tuple = ('GfG', 'for', 'Geeks')

# printing original tuple
print("The original tuple : " + str(test_tuple))

# using list comprehsion
# Rear elements from Tuple Strings
res = list(sub[len(sub) - 1] for sub in test_tuple)

# print result
print("The rear index string character list : " + str(res))
