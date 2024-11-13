# Python3 code to demonstrate working of
# Custom Tuple Key Summation in Dictionary
# Using sum() + generator expression

# initializing dictionary
test_dict = {('a', 'b'): 14, ('c', 'a'): 16, ('a', 'c'): 67, ('b', 'a'): 17}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing K
K = 'a'

# initializing index
idx = 1

# Custom Tuple Key Summation in Dictionary
# Using sum() + generator expression
res = sum(val for key, val in test_dict.items() if key[idx - 1] == K)

# printing result
print("The grouped summation : " + str(res))
