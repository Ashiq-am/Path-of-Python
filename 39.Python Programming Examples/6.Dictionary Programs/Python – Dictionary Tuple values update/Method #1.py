# Python3 code to demonstrate working of
# Dictionary Tuple values update
# Using generator expression + dictionary comprehension

# initializing dictionary
test_dict = {'Gfg': (5, 6), 'is': (7, 8), 'best': (10, 11)}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing K
# performing mutiplication by K
K = 3

# Dictionary Tuple values update
# Using generator expression + dictionary comprehension
res = {key: tuple(idx * K for idx in val)
       for key, val in test_dict.items()}

# printing result
print("The edited tuple values : " + str(res))
