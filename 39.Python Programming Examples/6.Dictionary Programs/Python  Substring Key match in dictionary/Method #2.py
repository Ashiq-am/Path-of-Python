# Python3 code to demonstrate working of
# Substring Key match in dictionary
# Using dict() + filter() + lambda

# initializing dictionary
test_dict = {'All' : 1, 'have' : 2, 'good' : 3, 'food' : 4}

# initializing search key string
search_key = 'ood'

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Using dict() + filter() + lambda
# Substring Key match in dictionary
res = dict(filter(lambda item: search_key in item[0], test_dict.items()))

# printing result
print("Key-Value pair for substring keys : " + str(res))
