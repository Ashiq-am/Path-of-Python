# Python3 code to demonstrate working of
# Remove Keys with K value
# Using dict() + filter() + lambda

# initializing dictionary
test_dict = {'Gfg': 6, 'is': 7, 'best': 9, 'for': 6, 'geeks': 11}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing K
K = 6

# employing lambda for computation
# filter() to perform filter according to lambda
res = dict(filter(lambda key: key[1] != K, test_dict.items()))

# printing result
print("The filtered dictionary : " + str(res))
