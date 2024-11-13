# Python3 code to demonstrate
# Nth column in Tuple Strings
# using list comprehension

# initializing tuple
test_tuple = ('GfG', 'for', 'Geeks')

# initializing N
N = 1

# printing original tuple
print("The original tuple : " + str(test_tuple))

# using list comprehsion
# Nth column in Tuple Strings
res = list(sub[N] for sub in test_tuple)

# print result
print("The Nth index string character list : " + str(res))
