# Python3 code to demonstrate working of
# Retain list elements value items
# Using filter() + lambda

# initializing dictionary
test_dict = {'gfg': 3, 'is': 2, 'best': 4, 'for': 7, 'geeks': 10}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing target list
tar_list = [3, 4, 10]

# Retain list elements value items
# Using filter() + lambda
res = dict(filter(lambda sub: sub[1] in tar_list, test_dict.items()))

# printing result
print("The filtered dictionary : " + str(res))
