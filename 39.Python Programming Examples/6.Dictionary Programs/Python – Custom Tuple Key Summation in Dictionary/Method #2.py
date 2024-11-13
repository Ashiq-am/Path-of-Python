# Python3 code to demonstrate working of
# Custom Tuple Key Summation in Dictionary
# Using sum() + map() + lambda

# initializing dictionary
test_dict = {('a', 'b'): 14, ('c', 'a'): 16, ('a', 'c'): 67, ('b', 'a'): 17}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing K
K = 'a'

# initializing index
idx = 1

# Custom Tuple Key Summation in Dictionary
# Using sum() + map() + lambda
res = sum(map(lambda sub: sub[1], filter(lambda ele: ele[0][idx - 1] == K,
                                         test_dict.items())))

# printing result
print("The grouped summation : " + str(res))
